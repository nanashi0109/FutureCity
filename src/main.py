from fastapi import FastApi, APIRouter
from .web import transport_handler, route_handler, citizen_handler, school

app = FastApi()

app.include_router(transport_handler.router)
app.include_router(route_handler.router)
app.include_router(citizen_handler)
app.include_router(school.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)