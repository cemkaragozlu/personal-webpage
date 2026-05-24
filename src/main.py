import fastapi
import os
from fastapi.staticfiles import StaticFiles
from src import index

import dotenv
dotenv.load_dotenv()

app = fastapi.FastAPI(
    title=os.environ["API_TITLE"],
    description=os.environ["API_DESCRIPTION"],
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(index.router)
