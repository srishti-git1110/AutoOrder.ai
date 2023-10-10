from multion_api import get_multion_output
from models import get_llm_output, get_vlm_output

import torch
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process-image/")
async def process_image(img: UploadFile):
    if not img.filename:
        return JSONResponse(content={"error": "No image file provided."}, status_code=400)

    image_bytes = await img.read()
    image_stream = BytesIO(image_bytes)
    img = Image.open(image_stream).convert('RGB')
<<<<<<< HEAD

=======
    
>>>>>>> 7dad3e8f71f4e3f8bac97ff199f7d3e2dbe59852
    img_description = get_vlm_output(img)
    instruction = get_llm_output(img_description)
    output = get_multion_output(instruction)
    
    return JSONResponse(content={"result": output})
