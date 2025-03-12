from fastapi import FastApi
from .web import transport_handler, route_handler, citizen_handler, mining


app = FastApi()

app.include_router(transport_handler.router)
app.include_router(route_handler.router)
app.include_router(citizen_handler)
app.include_router(mining.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)