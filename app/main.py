from fastapi import FastAPI

app = FastAPI(title="Sentinel Backend")

@app.get("/")
def root():
    return {"ok": True}
