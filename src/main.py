from fastapi import FastApi
from .web import transport_handler, route_handler, citizen_handler


app = FastApi()

app.include_router(transport_handler.router)
app.include_router(route_handler.router)
app.include_router(citizen_handler)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)