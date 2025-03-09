from fastapi import FastApi, APIRouter, Body

app = FastApi()




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)