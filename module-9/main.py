import requests
response = requests.get('http://dnd5eapi.co/api/conditions/blinded')
print(response.status_code)
print(response.json())d
