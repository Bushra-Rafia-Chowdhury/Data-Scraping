import requests
#BeautifulSoup will help us parse the HTML files
from bs4 import BeautifulSoup
from csv import writer

#For page 1
url1= 'https://www.scrapethissite.com/pages/forms/?page_num=1'
#Get the HTML
page1 =requests.get(url1)
# response 200 is successful responses
print(page1)
soup1= BeautifulSoup(page1.content, 'html.parser')
#now, all the html document inside soup1
#print(soup1)
lists1 = soup1.find_all('tr', class_="team")

#For page 2
url2= 'https://www.scrapethissite.com/pages/forms/?page_num=2'
page2 =requests.get(url2)
soup2= BeautifulSoup( page2.content, 'html.parser')
lists2 = soup2.find_all('tr', class_="team")

#For page 3
url3= 'https://www.scrapethissite.com/pages/forms/?page_num=3'
page3 =requests.get(url3)
soup3= BeautifulSoup( page3.content, 'html.parser')
lists3 = soup3.find_all('tr', class_="team")


with open('Bushra_Task2_Hockey_Teams.csv', 'w', encoding='utf8' , newline='') as f:
    w = writer(f)
    header = ['TeamName','Year','Wins','Losses','OTLosses','GoalFor_GF','GoalAgainst_GA']
    w.writerow(header)
    for i in lists1:
        TeamName = i.find('td', class_="name").text.replace('\n', '')
        Year = i.find('td', class_="year").text.replace('\n', '')
        Wins = i.find('td', class_="wins").text.replace('\n', '')
        Losses = i.find('td', class_="losses").text.replace('\n', '')
        OTLosses = i.find('td', class_="ot-losses").text.replace('', '').replace('\n', '')
        #Win_Parcentage = float(i.find('td', class_="pct text-success").text.replace('\n', ''))
        GoalFor_GF = i.find('td', class_="gf").text.replace('\n', '')
        GoalAgainst_GA = i.find('td', class_="ga").text.replace('\n', '')
        #plus_minus = float(i.find('td', class_="diff text-success").text.replace('\n', ''))

        # I'm unable to scraping this coulumn, because for this is a floating number type and
        # for this .text command, it's not showing all values of Win_Parcentage
        # error : AttributeError: 'NoneType' object has no attribute 'text'


        info1=[TeamName,Year,Wins,Losses,OTLosses,GoalFor_GF,GoalAgainst_GA]
        print(info1)
        w.writerow(info1)

    for i in lists2:
        TeamName = i.find('td', class_="name").text.replace('\n', '')
        Year = i.find('td', class_="year").text.replace('\n', '')
        Wins = i.find('td', class_="wins").text.replace('\n', '')
        Losses = i.find('td', class_="losses").text.replace('\n', '')
        OTLosses = i.find('td', class_="ot-losses").text.replace('', '').replace('\n', '')
        GoalFor_GF = i.find('td', class_="gf").text.replace('\n', '')
        GoalAgainst_GA = i.find('td', class_="ga").text.replace('\n', '')

        info2=[TeamName,Year,Wins,Losses,OTLosses,GoalFor_GF,GoalAgainst_GA]
        w.writerow(info2)

    for i in lists3:
        TeamName = i.find('td', class_="name").text.replace('\n', '')
        Year = i.find('td', class_="year").text.replace('\n', '')
        Wins = i.find('td', class_="wins").text.replace('\n', '')
        Losses = i.find('td', class_="losses").text.replace('\n', '')
        OTLosses = i.find('td', class_="ot-losses").text.replace('', '').replace('\n', '')
        GoalFor_GF = i.find('td', class_="gf").text.replace('\n', '')
        GoalAgainst_GA = i.find('td', class_="ga").text.replace('\n', '')

        info3=[TeamName,Year,Wins,Losses,OTLosses,GoalFor_GF,GoalAgainst_GA]
        w.writerow(info3)

