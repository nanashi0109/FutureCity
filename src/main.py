from fastapi import FastApi, APIRouter, Body

app = FastApi()


@app.get()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)