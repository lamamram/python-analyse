# %%
import requests
from time_context import TimerCtx
from concurrent.futures import ThreadPoolExecutor as TPE
from multiprocessing import cpu_count
from functools import reduce

class GoRestApi:
    __URL = "https://gorest.co.in/public"
    __NB_WORKERS = cpu_count()

    def __init__(self, version="v2") -> None:
        self.__version = version

    def __call(self, method, endpoint, data={}, headers={}, files={}):
        response = {"valid": True, "response": None}
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

    def get_user_page(self, page_id):
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
            # le map est synchrone
            results = pool.map(self.get_user_page, list(range(start, stop + 1, step)))
            responses = list(map(lambda r: r["response"] if r["valid"] else [], results))
            return reduce(lambda x, y : x + y, responses)
        # for i in range(start, stop + 1, step):
        #     obj = self.get_user_page(i)
        #     if obj["valid"]:
        #         data += obj["response"]
        #     print(f"page {i} fetched")
        return data

    def get_version(self):
        return self.__version


if __name__ == "__main__":
    api = GoRestApi()
    with TimerCtx():
        # print(len(api.get_user_pages(10)))
        print(len(api.get_user_pages_async(100)))
# %%
