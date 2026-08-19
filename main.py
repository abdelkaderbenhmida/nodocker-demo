from fastapi import FastAPI

app = FastAPI(title="No-Dockerfile Demo")

@app.get("/")
def root():
    return {"hello": "from a repo with no Dockerfile"}
