from fastapi import FastApi, APIRouter
from .web import transport_handler, route_handler


app = FastApi()

app.include_router(transport_handler.router)
app.include_router(route_handler.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)