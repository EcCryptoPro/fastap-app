from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API rodando com sucesso via Render!"}
