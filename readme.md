  
 # h1Tracker 

 This project includes scraping hackerone.com,  extracting all the published reports and hosting it on a website.

## The Scraper
 "H1WebscraperforDB.py" scrapes hackerone.com to extract all the published reports in JSON format and store the required details in a database named "h1Reports.db" using sqlite3.

 The URL "https://hackerone.com/reports/{i}" is used for scraping, where "i" is a variable ranging from 1 to the Report ID of the latest published report (2302094 at the time of writing this) in hackerone.com. 

 ## The Website
 "app.py" is the web app made with the flask framework.
 
 ** All the info in this website are based only on the reports published by hackerone.com.**

 The homepage consists of the following tables and pie charts:
 1. Top 10 Bounties - Table
 2. Top 10 Reported Weaknesses - Table
 3. Top 10 Rewarded Weaknesses - Table
 4. Top 10 Reported Programs - Table
 5. Top 10 Rewarding Programs - Table
 6. Top 10 Reporters - Table
 7. Top 10 Earners - Table
 8. Top Earnings per Program Pie Chart
 9. Top Earnings per Weakness Pie Chart

 The Top Nav Bar consists of links to the following pages:
 ### Published Reports - /publishedReports/
This page displays all the published reports. It includes:

#### * Report ID
The "Report ID" is linked to the page "/publishedReports/ReportID" which displays the following details:
* ReportID (This is linked to that particular report in hackerone.com "https://hackerone.com/reports/'ReportID'")
* Title (Title of the report)
* Program (This is linked to "/allPrograms/'Program'" which displays all the published reports of that particular program)
* Reported by (This is linked to "/allReporters/'Reporter'" which displays all the published reports of that particular Reporter)
* Weakness (This is linked to "/allWeaknesses/'Weakness'" which displays all the published reports of that particular Weakness)
* Bounty($) (Bounty reward amount, if any)
* Severity (Severity of the vulnerability reported)
* Description (FIrst few paragraphs of the report)
#### * Title of the report

#### * Type of Weakness reported
This is linked to "/allWeaknesses/'Weakness'" which displays all the published reports of that particular Weakness.
#### * Program name
This is linked to "/allPrograms/'Program'" which displays all the published reports of that particular Program.
#### * Reporter
This is linked to "/allReporters/'Reporter'" which displays all the published reports of that particular Reporter.

### Programs - /allPrograms/
 This page displays all the Programs in hackerone.com.
 It includes:
#### * Program name 
  This is linked to "/allPrograms/'Program'" which displays all the published reports of that particular Program.
#### * Number of Reports published relating to that particular program

### Reporters- /allReporters/
This page displays all the Programs in hackerone.com.
 It includes:
#### * Reporter name 
  This is linked to "/allReporters/'Reporter'" which displays all the published reports of that particular Reporter.
#### * Number of published Reports reported by that particular reporter

### Weaknesses - /allWeaknesses/
This page displays all the Weaknesses reported in hackerone.com.
It includes:
#### * Weakness name
This is linked to "/allWeaknesses/'Weakness'" which displays all the published reports of that particular Weakness.
#### * Number of published Reports reported on that particular weakness


 
