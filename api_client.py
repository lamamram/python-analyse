# %%
import requests
from time_context import TimerCtx
from concurrent.futures import ThreadPoolExecutor as TPE, as_completed
from multiprocessing import cpu_count
from functools import reduce
from time import sleep
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN=os.environ["TOKEN"]

# décorateur: retourne une fonction qui ajoute in comportement
# à une fonction en paramètre
def delayed(f):
    def wrapper(*a, **kwd):
        delay = a[2] if len(a) > 2 else 0
        sleep(delay)
        return f(*a, **kwd)
    return wrapper

class GoRestApi:
    __URL = "https://gorest.co.in/public"
    __NB_WORKERS = cpu_count()

    def __init__(self, token=TOKEN, version="v2") -> None:
        self.__version = version
        self.__token = token

    def __call(self, method, endpoint, data={}, headers={}, files={}):
        response = {"valid": True, "response": None}
        if method.upper() in ("POST", "PUT", "PATCH", "DELETE"):
            headers["Authorization"] = f"Bearer {self.__token}"
        try:
            location = f"{self.__URL}/{self.__version}/{endpoint}"
            call_fn = getattr(requests, method.lower())
            r = call_fn(
                location, 
                data=data, 
                headers=headers, 
                files=files
            )
            if 200 <= r.status_code < 300:
                # réponse json
                if "application/json" in r.headers["content-type"]:
                    response["response"] = r.json()
                elif "text/" in r.headers["content-type"]:
                    response["response"] = r.text.decode(r.encoding)
                # réponse octets => images et autres téléchargements
                else:
                    response["response"] = r.content
            else: raise ValueError(f"wrong status {r.status_code}")
        except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
            # raise type(e)
            response["valid"] = False
            response["response"] = e
        return response

    # équivalent à get_user_page = delayed(get_user_page)
    @delayed
    def get_user_page(self, page_id, *a):
        return self.__call("GET", f"users?page={page_id}")

    def get_user_pages(self, *args):
        data = []
        start = args[0] if len(args) > 1 else 1
        stop = args[0] if len(args) == 1 else args[1]
        step = args[2] if len(args) > 2 else 1
        for i in range(start, stop + 1, step):
            obj = self.get_user_page(i)
            if obj["valid"]:
                data += obj["response"]
            print(f"page {i} fetched")
        return data
    
    def get_user_pages_async(self, *args, nb_workers=None):
        if not nb_workers: nb_workers = self.__NB_WORKERS
        data = []
        start = args[0] if len(args) > 1 else 1
        stop = args[0] if len(args) == 1 else args[1]
        step = args[2] if len(args) > 2 else 1
        with TPE(max_workers=nb_workers) as pool:
            ## map synchrone
            # args = [ i for i in range(start, stop+1, step)]
            args = [ (i, (i - 1)*0.05) for i in range(start, stop + 1, step) ]
            results = pool.map(lambda a: self.get_user_page(*a), args)
            responses = list(map(lambda r: r["response"] if r["valid"] else [], results))
            return reduce(lambda x, y : x + y, responses)

            ## liste d'objets asynchrones dépilés dans l'ordre d'arrivée
            # futs = [pool.submit(self.get_user_page, i) for i in range(start, stop+1, step)]
            # for f in as_completed(futs):
            #     data.append(f.result())
        # for i in range(start, stop + 1, step):
        #     obj = self.get_user_page(i)
        #     if obj["valid"]:
        #         data += obj["response"]
        #     print(f"page {i} fetched")
        return data

    def get_version(self):
        return self.__version
    
    def create_user(self, user):
        return self.__call("POST", "users", data=user)


if __name__ == "__main__":
    api = GoRestApi()
    with TimerCtx():
        # print(len(api.get_user_pages(10)))
        print(len(api.get_user_pages_async(10)))
        # user = {
        #     "name": "mlamam",
        #     "email": "admin@example.com",
        #     "gender": "male",
        #     "status": "active"
        # }
        # print(api.create_user(user))
# %%
