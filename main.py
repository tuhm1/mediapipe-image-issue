from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
from PIL import Image
import mediapipe as mp
import numpy as np
import tempfile
import shutil

app = FastAPI()

detector = mp.tasks.vision.ObjectDetector.create_from_options(
    mp.tasks.vision.ObjectDetectorOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path="model.tflite"),
        score_threshold=0.5,
        running_mode=mp.tasks.vision.RunningMode.IMAGE
    )
)

@app.post("/api/image-from-ndarray")
def detect(file: UploadFile):
    with Image.open(file.file) as image:
        np_data = np.asarray(image)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_data)
        result = detector.detect(mp_image)
        return result
    

@app.post("/api/image-from-file")
def detect(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp.close()
        mp_image = mp.Image.create_from_file(tmp.name)
        result = detector.detect(mp_image)
        return result
    
app.mount("/", StaticFiles(directory=".", html=True))
