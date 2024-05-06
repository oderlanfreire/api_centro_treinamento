from fastapi import FastAPI
import uvicorn

app = FastAPI(title="centro de treinamento api")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info", reload=True)

