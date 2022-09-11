from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello!"

if __name__ == "__app__":
    uvicorn.run(app, host ='localhost', port = 8000)