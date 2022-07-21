# %%
import os
from dotenv import load_dotenv

load_dotenv()

sharepoint_conn = {
    "HOST": os.environ["SHAREPOINT_HOST"],
    "USER": os.environ["SHAREPOINT_USER"],
    "PWD": os.environ["SHAREPOINT_PWD"],
}


sharepoint_conn
# {k: v for k, v in os.environ.items()}
# %%
