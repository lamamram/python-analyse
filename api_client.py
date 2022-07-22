# %%
import requests

class GoRestApi:
    __URL = "https://gorest.co.in/public"

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
            else: raise ValueError(f"wrong status {r.status_code}: {r.text}")
        except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
            # raise type(e)
            response["valid"] = False
            response["response"] = e
        return response

    def get_user_page(self, page_id):
        return self.__call("GET", f"users?page={page_id}")

    def get_version(self):
        return self.__version


if __name__ == "__main__":
    api = GoRestApi()
    print(api.get_user_page(1))
# %%
