from fastapi import FastAPI, APIRouter
from .web import transport, route, citizen, school


app = FastAPI()

app.include_router(transport.router)
app.include_router(route.router)
app.include_router(citizen.router)
app.include_router(school.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)