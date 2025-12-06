import requests
import json

# Test what endpoints are actually working
endpoints = ['/health', '/genz-preview', '/anonymize', '/deanonymize']

for endpoint in endpoints:
    try:
        response = requests.get(f'http://localhost:3000{endpoint}', timeout=2)
        print(f"{endpoint}: Status {response.status_code}")
        if response.status_code == 200:
            print(f"  Response: {response.text[:100]}")
    except requests.exceptions.RequestException as e:
        print(f"{endpoint}: Error - {e}")
    print("-" * 50)
