from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()


Model = tf.keras.models.load_model("/fruits_CNN_V05.h5")
CLASS_NAMES = ["apple", "avocado", "banana", "kiwi", "lemon", "orange"]

@app.get("/ping")
async def ping():
    return "Hello!"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, 0)
    oredictions = Model.predict(image_batch)

    pass


if __name__ == "__main__":
    uvicorn.run(app, host ='localhost', port = 5000)