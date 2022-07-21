# %%
import os
from dotenv import load_dotenv

load_dotenv()

sharepoint_conn = {
    "URL": os.environ["SHAREPOINT_URL"],
    "USER": os.environ["SHAREPOINT_USER"],
    "PWD": os.environ["SHAREPOINT_PWD"],
}


sharepoint_conn
# {k: v for k, v in os.environ.items()}
# %%
from office365.sharepoint.client_context import ClientContext

ctx = ClientContext(sharepoint_conn["URL"])
ctx.with_user_credentials(sharepoint_conn["USER"], sharepoint_conn["PWD"])
web = ctx.web.get().execute_query()


#save data to BytesIO stream
# bytes_file_obj = io.BytesIO()
# bytes_file_obj.write(response.content)
# bytes_file_obj.seek(0)