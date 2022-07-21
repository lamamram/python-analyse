# %%
import os
from dotenv import load_dotenv

load_dotenv()

sharepoint_conn = {
    "HOST": os.environ["SHAREPOINT_HOST"],
    "PATH": os.environ["SHAREPOINT_PATH"],
    "USER": os.environ["SHAREPOINT_USER"],
    "PWD": os.environ["SHAREPOINT_PWD"],
}


sharepoint_conn
# {k: v for k, v in os.environ.items()}
# %%
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

ctx_auth = AuthenticationContext(sharepoint_conn["HOST"])
ctx_auth.acquire_token_for_user(sharepoint_conn["USER"], sharepoint_conn["PWD"])
ctx = ClientContext(sharepoint_conn["HOST"], ctx_auth)
ctx.load(ctx.web)
ctx.execute_query()
response = File.open_binary(ctx, sharepoint_conn["PATH"])


#save data to BytesIO stream
# bytes_file_obj = io.BytesIO()
# bytes_file_obj.write(response.content)
# bytes_file_obj.seek(0)