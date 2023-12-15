from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

#reportID = 110
#1starting at report #110
#2286094
def main(reportID):
    driver = webdriver.Chrome()
    driver.get(f"https://hackerone.com/reports/{reportID}")

    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html,'html.parser')
    #print(soup)

    def scrape():
        reports = soup.find_all('div', 'report-with-metadata-sidebar')

        for report in reports:
            title = report.find('div', 'false report-heading__report-title break-all spec-report-title').text
            id = report.find('div', 'report-status').text
            userName = report.find('span', itemprop="name").text
            category = report.find('div', 'sc-aXZVg egBYvJ new-metadata-item spec-weakness-meta-item').text
            bounty = report.find('div', 'sc-aXZVg egBYvJ new-metadata-item spec-bounty-amount-meta-item').text
            severity = report.find('div', 'sc-aXZVg egBYvJ new-metadata-item spec-report-severity-meta-item').text
            summary = report.find('div', 'spec-vulnerability-information timeline-container-content').text
            #//*[@class='sc-aXZVg egBYvJ new-metadata-item spec-bounty-amount-meta-item']
            print(f'Report Id: {id}')
            print(f'Report Title: {title}')
            print(f'Reporter: {userName}')
            print(f'Category: {category}')
            print(bounty)
            print(severity)
            print(summary)

    while soup.find('title').text != 'Page not found | HackerOne':
        if soup.find('title').text == 'Access denied | HackerOne' or soup.find('title').text == 'Sign in | HackerOne' :
            reportID+=1
            #print(reportID)
            main(reportID)
        else:
            scrape()
            reportID += 1
            #print(reportID)
            main(reportID)
            break
    else:
        print('*****************************\n\t+++FINISHED+++\n*****************************')
main(110)
