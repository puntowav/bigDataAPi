from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def get_root():
    return("esto es la root")

@app.get("/iAvall")
def get_iAvall():
    return("esto es la iAvall")