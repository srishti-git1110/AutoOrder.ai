# AutoOrder.ai
AutoOrder is a powerful AI-driven automation tool that streamlines tasks using image-based instructions. It combines cutting-edge Vision and Language Models (VLM and LLM) to transform images into actionable human-like commands, making automation more intuitive and accessible. Whether you need to order food, book tickets, or perform any online task, AutoOrder simplifies it all through the magic of artificial intelligence.

With AutoOrder, you can upload an image, and the system generates detailed descriptions. It then converts these descriptions into natural language instructions using advanced language models. These instructions can be used to automate tasks across the web, reducing the need for manual intervention. Say goodbye to tedious form-filling and step-by-step online processes; AutoOrder turns images into action!


A FastAPI endpoint that takes an input image (a chat screenshot, a food/clothing item etc.) and automates browser actions accordingly using the MultiON API.
It is able to automate actions like scheduling meetings based on a chat's ss, ordering a food dish by only using its image etc.

## Usage
To run the API, clone the repository and run the following in the terminal -
```
pip install uvicorn
uvicorn app:app --reload

```

