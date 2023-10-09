from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from prompts import get_llm_prompt
from prompts import get_vlm_prompt

import torch
from PIL import Image


app = FastAPI()

# the endpoint to receive image uploads
@app.post("/process-image/")
async def process_image(img: UploadFile):
    
    if img is None:
        return JSONResponse(content={"error": "No image file provided."}, status_code=400)

    text_commands = []

    for file in files:
        # Process each image and generate text
        text = process_image_to_text(file)
        text_commands.append(text)

    # Step 2: MultiOn API
    # Use text_commands to interact with MultiOn API and get results
    results = []

    for command in text_commands:
        result = interact_with_multion_api(command)
        results.append(result)

    # Step 3: Return the results
    return JSONResponse(content={"results": results})

# Helper functions for processing images and interacting with the MultiOn API
def process_image_to_text(file: UploadFile):
    # Implement image processing and text generation logic here
    pass

def interact_with_multion_api(command: str):
    # Implement logic to interact with the MultiOn API using the command
    pass

