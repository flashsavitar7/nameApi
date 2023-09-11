import requests

base_url = 'https://nameapi-mnmf.onrender.com/api'  # Update with your API URL

# Test CREATE operation
create_response = requests.post(base_url, json={"name": "John Doe"})
try:
    print("CREATE operation:")
    print(create_response.json())
except requests.exceptions.JSONDecodeError:
    print("Non-JSON response received:")
    print(create_response.text)

# Test READ operation
get_response = requests.get(f'{base_url}/1')
print("\nREAD operation:")
print(get_response.json())

# Test UPDATE operation
update_response = requests.put(f'{base_url}/1', json={"name": "Jane Doe"})
print("\nUPDATE operation:")
print(update_response.json())

# Test DELETE operation
delete_response = requests.delete(f'{base_url}/1')
print("\nDELETE operation:")
print(delete_response.json())
