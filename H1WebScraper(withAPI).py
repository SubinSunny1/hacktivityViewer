import requests

#reportID = 110

for i in range(5442,2999999):
    url = f"https://api.hackerone.com/v1/hackers/reports/{i}"
    headers = {
        'Accept': 'application/json',
    }
    auth = ('dolphin123', 'CvvNMseXxmDtglVmwKwmMizKNi7EZJmE0h5+Yctzwg0=')

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        output = response.json()
        try:
            print(f"ReportID: {output['data']['id']}")
        except:
            print("ReportID: Nil")
        try:
            print(f"Report Title: {output['data']['attributes']['title']}")
        except:
            print("Report Title: Nil")
        try:
            print(f"Reporter: {output['data']['relationships']['reporter']['data']['attributes']['username']}")
        except:
            print("Reporter: Nil")
        try:
            print(f"Category: {output['data']['relationships']['weakness']['data']['attributes']['name']}")#not available in some reports
        except:
            print("Category:Nil")
        try:
            print(f"Bounty: {output['data']['relationships']['bounties']['data'][0]['attributes']['amount']}")
        except:
            print("Bounty: Nil")
        try:
            print(f"Severity: {output['data']['relationships']['severity']['data']['attributes']['rating']}")
        except:
            print("Severity: Nil")
        try:
            print(f"Description: {output['data']['relationships']['weakness']['data']['attributes']['description']}")
        except:
            print("Description: Nil")
        print('\n')

    elif response.status_code == 403:
        #print(f"Report not public")
        pass

    else:
        #print("+++++++++++End of Reports+++++++++++")
        #print(response.text)
        #quit()
        pass
print("+++++++++++End of Reports+++++++++++")
