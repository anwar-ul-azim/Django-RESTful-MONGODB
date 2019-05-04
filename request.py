import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTUyNDAwMDgzLCJqdGkiOiJjYzNmMjk2ODk4YmY0NjRmYWVjZmE3NjRkNmQ5OTBhNCIsInVzZXJfaWQiOjF9.l1GZGYyjXadhs4BWbGnMw-yco9JCvovZrWEdrpyq2Js'

request = requests.get('http://localhost:8000/category/', headers=headers)

print(request.text)
