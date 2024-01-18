import requests

url = "https://hackerone.com/reports/1553.json"
headers = {
    'Accept': 'application/json',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    output = response.json()
    try:
        print(f"ReportID: {output['id']}")
    except:
        print("ReportID: Nil")
    try:
        print(f"Report Title: {output['title']}")
    except:
        print("Report Title: Nil")
    try:
        print(f"Reported to: {output['team']['profile']['name']}")
    except:
        print("Reported to: Nil")            
    try:
        print(f"Reporter: {output['reporter']['username']}")
    except:
        print("Reporter: Nil")
    try:
        print(f"Category: {output['weakness']['name']}")
    except:
        print("Category:Nil")
    try:
        print(f"Bounty: ${output['bounty_amount']}")
    except:
        print("Bounty: Nil")
    try:
        print(f"Severity: {output['severity_rating']}")
    except:
        print("Severity: Nil")
    try:
        print(f"Summary: \n\t{output['summaries'][0]['content']}")
    except:
        print("Summary: Nil")

elif response.status_code == 403:
    #print(f"Report not public")
    pass

else:
    print("End of Reports")
    print(response.text)
    #break
