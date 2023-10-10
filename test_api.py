import requests

url = 'http://127.0.0.1:8000/process-image'
files = {'img': ('pizza.jpg', open('C:/Users/hp/Downloads/pizza.jpg', 'rb'))}

response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
