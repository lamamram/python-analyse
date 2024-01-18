# %%
import requests

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
        for i in range(page_start, page_end):
            ret["data"].append(self.get_user(i))
            

if __name__ == "__main__":
    api = GorestClient()
    print("100 pages synchrones:")
    print(api.get_users_pages(1, 100))

# %%
