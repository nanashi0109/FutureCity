from fastapi import FastApi, APIRouter
from .web import transport, route, citizen


app = FastApi()

app.include_router(transport.router)
app.include_router(route.router)
app.include_router(citizen.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)