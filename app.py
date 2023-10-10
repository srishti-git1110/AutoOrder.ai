from multion_api import get_multion_output
from models import get_llm_output, get_vlm_output

import torch
from PIL import Image
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process-image/")
async def process_image(img: UploadFile):
    if not img.filename:
        return JSONResponse(content={"error": "No image file provided."}, status_code=400)

    img = Image.open(img).convert('RGB')
    img_description = get_vlm_output(img)
    instruction = get_llm_output(img_description)
    output = get_multion_output(instruction)
    
    return JSONResponse(content={"result": output})