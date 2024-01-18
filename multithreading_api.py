# %%
import requests
from time import time
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor as TPE, as_completed

URL = "https://gorest.co.in/public"

ERRORS = (
    AttributeError, 
    requests.ConnectionError, 
    requests.HTTPError,
    ValueError)

class GorestClient:
    def __init__(self, version="v2"):
        self.__version = version
        self.__session = requests.Session()
    
    def __call(self, method, endpoint, data={}, headers={}, files={}):
        response = {"valid": True}
        url = f"{URL}/{self.__version}/{endpoint}"
        try:
            r = self.__session.send(
                requests.Request(method, url, data=data, headers=headers, files=files).prepare()
            )
            # tester le code de retour
            if 200 <= r.status_code < 300:
                # formater le corps de la réponse en fonction des entêtes de réponse
                if "json" in r.headers["content-type"]:
                    response["data"] = r.json()
                elif "text/" in r.headers["content-type"]:
                    response["data"] = r.text.decode(r.encoding)
                else:
                    response["data"] = r.content
            else: raise ValueError(f"Wrong status: {r.status_code}: {r.json()['message']}")
        except ERRORS as e:
            response["valid"] = False
            response["data"] = e
        return response
    
    def get_user(self, page):
        print(f"page {page} fetched")
        return self.__call("GET", f"users?page={page}")

    def get_users_pages(self, page_start, page_end):
        ret = {"data": [], "errors": []}
        # SYNCHRONE
        # for i in range(page_start, page_end):
        #     ret["data"].append(self.get_user(i))
        # return ret
        # initialise le pool avec ici la moitié des cpus
        with TPE(cpu_count()//2) as pool:
            ## SUBMIT un appel particulier de la pool qui retourne un objet Future
            # futs = [
            #     pool.submit(self.get_user, p) for p in range(page_start, page_end + 1)
            # ]
            # as_completed attends que les résultats sont arrivés
            # for f in as_completed(futs):
            #     # f.result() rend les données où rien si les donnée ne sont pas encore reçu
            #     ret["data"].append(f.result())

            ## MAP: lance des appels sur le même worker mais avec des paramètrages différents
            # on peut donner autants de paramètres 
            # car la pool les appels supplémentaires sont mis en file d'attente
            # la map retourne un iterateur synchrone 
            ret["data"] += pool.map(
                self.get_user,
                # [(),(),()] si le worker a besoin de plusieurs workers
                list(range(page_start, page_end + 1))
            )
        return ret

        
            

if __name__ == "__main__":
    api = GorestClient()
    print("20 pages asynchrones:")
    start = time()
    print(api.get_users_pages(1, 20))
    print(round(time() - start, 3))
# %%
