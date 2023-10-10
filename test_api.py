import argparse
import os
import requests

def main():
    parser = argparse.ArgumentParser(description='Test the FastAPI API with an image file.')
    parser.add_argument('image_path', type=str, help='Path to the image file on your local system')
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: The file '{args.image_path}' does not exist.")
        return

    url = 'http://127.0.0.1:8000/process-image'
    files = {'img': (os.path.basename(args.image_path), open(args.image_path, 'rb'))}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        print("API response:")
        print(response.json())
    else:
        print(f"API request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()
