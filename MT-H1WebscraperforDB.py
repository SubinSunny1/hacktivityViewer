import requests
from concurrent.futures import ThreadPoolExecutor
import time 

id = None
title = None
client = None
reporter = None
category = None
bountyUSD = None
severity = None
description = None
no_of_reports = 0
#110
#2302094
def fetch_report(id):
    time.sleep(3)
    url = f"https://hackerone.com/reports/{id}"
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        output = response.json()
        try:
            print(f"ReportID: {output['id']}")
            #id =  output['id']
            #print(id)

        except:
            print("ReportID: Nil")
            #pass
        try:
            print(f"Report Title: {output['title']}")
            #title = output['title']
            #print(title)
        except:
            print("Report Title: Nil")
            #pass
        try:
            print(f"Reported to: {output['team']['profile']['name']}")
            #client = output['team']['profile']['name']
            #print(client)
        except:
            print("Reported to: Nil")            
            #pass
        try:
            print(f"Reporter: {output['reporter']['username']}")
            #reporter = output['reporter']['username']
            #print(reporter)
        except:
            print("Reporter: Nil")
            #pass
        try:
            print(f"Category: {output['weakness']['name']}")
            #category = output['weakness']['name']
            #print(category)
        except:
            print("Category:Nil")
            #pass
        try:
            print(f"Bounty: ${output['bounty_amount']}")
            #bountyUSD = output['bounty_amount']
            #print(bountyUSD)
        except:
            print("Bounty: Nil")
            #pass
        try:
            print(f"Severity: {output['severity_rating']}")
            #severity = output['severity_rating']
            #print(severity)
        except:
            print("Severity: Nil")
            #pass
        try:
            print(f"Description: \n\t{output['vulnerability_information']}")#['summaries'][0]['content']
            #description = output['vulnerability_information']
            #print(description)
        except:
            print("Description: Nil")
            #pass
        print('\n')
        no_of_reports +=1
    #elif response.status_code == 403:
        #print(f"Report not public")
    #    pass

    else:
        #print(f"Report {id} not public")
        #print(response.status_code)
        #quit()
        pass
    print(no_of_reports)


def main():
    report_ids = range(110,501)
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(fetch_report, report_ids)
    
    return results

if __name__== '__main__':
    main()


print("+++++++++++End of Reports+++++++++++")
