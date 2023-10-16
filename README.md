# AutoOrder.ai
AutoOrder is a powerful AI-driven automation tool that automates tasks like ordering food from doordash, buying things from amazon etc. All you need to enter is an image of the product you want to get ordered and rest all is automated!

It combines cutting-edge Vision and Language Models (VLM and LLM) to transform images into actionable human-like instructions that are ingested by the MultiON API which is the backbone of this project. Whether you need to order food, book tickets, or perform any online task, MultiON can do it all, and this project integrates it with the power of VLMs and LLMs to let the user automate browser actions using just images.

As of now, the repository implements a FastAPI endpoint that takes an input image (a chat screenshot, a food/clothing item etc.) and automates browser actions accordingly using the MultiON API.

## Table of Contents
* [Installation](https://github.com/srishti-git1110/AutoOrder_ai#installation)
* [Usage](https://github.com/srishti-git1110/AutoOrder_ai#usage)
* [Testing](https://github.com/srishti-git1110/AutoOrder_ai#testing)
* [API Endpoints](https://github.com/srishti-git1110/AutoOrder_ai#api-endpoints)
* [Contributing](https://github.com/srishti-git1110/AutoOrder_ai#contributing)
* [License](https://github.com/srishti-git1110/AutoOrder_ai#license)

## Installation
To run the MultiON API on your local machine, follow these steps:

1. Clone the repository:
```
git clone https://github.com/srishti-git1110/AutoOrder_ai.git
cd AutoOrder_ai
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the project dependencies:
```
pip install -r requirements.txt
pip install uvicorn
```

4. You'll also need an OpenAI API key for this in a .env file in the project's root directory. Make sure to create this file and enter your key as an environment variable.

## Usage
1. Start the FastAPI application using Uvicorn:
```
uvicorn app:app --reload
```
This will launch the API locally at http://127.0.0.1:8000.

2. Open a web browser or use an API testing tool (e.g., Postman or curl) to interact with the API.

## Testing
You can use the provided test_api.py script to test the API with an image file. Simply run the script from the command line and provide the path to the image file as an argument:

```
python test_api.py --image_path /path/to/your/image.jpg
```

The script will send a POST request to the API, providing the image for processing. It will then automate the browser actions accordingly.

## API Endpoints
The AutoOrder API has one main endpoint:

* `POST /process-image`: Upload an image for processing and automate the browser actions accordingly.
The API expects the image to be uploaded using the img field in a multipart/form-data request.

## Contributing
If you'd like to contribute to this project, please follow these steps:

* Fork the repository on GitHub.
* Create a new branch for your feature or bug fix.
* Make your changes and submit a pull request.

Contributions are very much welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
