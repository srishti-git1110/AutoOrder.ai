from config import config
from prompts import get_vlm_prompt, get_llm_prompt

import torch
import openai 
from transformers import (
    BitsAndBytesConfig,
    InstructBlipProcessor, 
    InstructBlipForConditionalGeneration,
)

openai.api_key = config.openai_api_key
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_vlm_output(img):
    double_quant_config = BitsAndBytesConfig(load_in_4bit=True,
                                             bnb_4bit_quant_type="nf4",
                                             bnb_4bit_use_double_quant=True,
                                             bnb_4bit_compute_dtype=torch.bfloat16)
    
    processor = InstructBlipProcessor.from_pretrained(
        "Salesforce/instructblip-vicuna-7b",
        quantization_config=double_quant_config
    )
    model = InstructBlipForConditionalGeneration.from_pretrained(
        "Salesforce/instructblip-vicuna-7b",
        quantization_config=double_quant_config
    )
    
    prompt = get_vlm_prompt()

    inputs = processor(images=img, text=prompt, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_new_tokens=200)
    img_description = processor.batch_decode(out, skip_special_tokens=True)[0].strip()

    return img_description

def get_llm_output(img_description):
    prompt = get_llm_prompt()

    completion = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=250,
      temperature=0.7,
      top_p=1.0,
      stop="[eot]")

    return (completion.choices[0].text)





