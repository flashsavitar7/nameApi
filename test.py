import requests

base_url = 'https://nameapi-mnmf.onrender.com/api'  # Update with your API URL

create_response = requests.post(base_url, json={"name": "John Doe"})
try:
    print(create_response.json())
except requests.exceptions.JSONDecodeError:
    print("Non-JSON response received:")
    print(create_response.text)

get_response = requests.get(f'{base_url}/John Doe')
print("\nREAD operation:")
print(get_response.json())


update_response = requests.put(f'{base_url}/John Doe', json={"name": "Jane Doe"})
print("\nUPDATE operation:")
print(update_response.json())


delete_response = requests.delete(f'{base_url}/Jane Doe')
print("\nDELETE operation:")
print(delete_response.json())
