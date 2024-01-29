import requests
import sqlite3

conn = sqlite3.connect('h1Reports.db')
c = conn.cursor()

#c.execute('''CREATE TABLE
#        report(id TEXT, title TEXT, client TEXT, reporter TEXT,
#       category TEXT, bounty FLOAT, severity TEXT, description TEXT)''')

#reportID = 110

#110
#2302094
for i in range(1286351,2302094):
    id = None
    title = None
    client = None
    reporter = None
    category = None
    bounty = None
    severity = None
    description = None

    url = f"https://hackerone.com/reports/{i}"
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        output = response.json()
        try:
            #print(f"ReportID: {output['id']}")
            id =  output['id']
            #print(id)

        except:
            #print("ReportID: Nil")
            pass
        try:
            #print(f"Report Title: {output['title']}")
            title = output['title']
            #print(title)
        except:
            #print("Report Title: Nil")
            pass
        try:
            #print(f"Reported to: {output['team']['profile']['name']}")
            client = output['team']['profile']['name']
            #print(client)
        except:
            #print("Reported to: Nil")            
            pass
        try:
            #print(f"Reporter: {output['reporter']['username']}")
            reporter = output['reporter']['username']
            #print(reporter)
        except:
            #print("Reporter: Nil")
            pass
        try:
            #print(f"Category: {output['weakness']['name']}")
            category = output['weakness']['name']
            #print(category)
        except:
            #print("Category:Nil")
            pass
        try:
            #print(f"Bounty: ${output['bounty_amount']}")
            bounty = output['bounty_amount']
            #print(bounty)
        except:
            #print("Bounty: Nil")
            pass
        try:
            #print(f"Severity: {output['severity_rating']}")
            severity = output['severity_rating']
            #print(severity)
        except:
            #print("Severity: Nil")
            pass
        try:
            #print(f"Description: \n\t{output['vulnerability_information']}")#['summaries'][0]['content']
            description = output['vulnerability_information']
            #print(description)
        except:
            #print("Description: Nil")
            pass
        #print('\n')
        #print(id,'\n', title,'\n', client,'\n', reporter,'\n', category,'\n', bountyUSD,'\n', severity,'\n', description)

        c.execute('''INSERT INTO report VALUES(?,?,?,?,?,?,?,?)''', (id,title,client,reporter,category,bounty,severity,description))
        conn.commit()
        #print('complete')
        #c.execute('''SELECT * FROM report''')
        #results = c.fetchall()
        #print(results)
        print(f"Report {i}--{response.text}")


        #conn.close()

    #elif response.status_code == 403:
        #print(f"Report not public")
    #    pass

    else:
        #print("+++++++++++End of Reports+++++++++++")
        print(f"Report {i}--{response.text}")
        #quit()
        pass
print("+++++++++++End of Reports+++++++++++")
