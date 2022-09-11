from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello!"

if __name__ == "__app__":
    uvicorn.run(app, host ="127.8.0.0.0.1", port = 8000)