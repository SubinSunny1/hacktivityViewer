import requests

url = "https://api.hackerone.com/v1/hackers/reports/110"
headers = {
    'Accept': 'application/json',
}
auth = ('userid', 'UUID')

response = requests.get(url, headers=headers, auth=auth)

if response.status_code == 200:
    # Print or process the response content
    print(response.json())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
