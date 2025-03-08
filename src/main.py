from fastapi import FastApi

app = FastApi()

#TODO: include routers


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)