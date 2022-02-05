#Requests for sending requests to the HTML and get some responds
import requests
#BeautifulSoup will help us parse the HTML files
from bs4 import BeautifulSoup
from csv import writer

url= 'https://www.psychologytoday.com/us/therapists/10956?zipdist=2&fbclid=IwAR2qm-vECbZmDa7SwHG2PyKX2C716zdvkN_hKDN1xAWLL0JmiJYYDM8FDT0'

#Get the HTML
page =requests.get(url)
print(page)
# Here, the output shows <Response [403]>
#It means that, Client error responses, Details: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
#If it is in between (200–299), then it can be Successful responses page and then it can be scraped.
#So, this link can't be Scraped.