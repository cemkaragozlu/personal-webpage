from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
def main():
    return FileResponse("src/static/index.html")
