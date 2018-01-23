import requests
from bs4 import BeautifulSoup
import csv
import texttable as tt

tab = tt.Texttable()
url = "http://www.bankmuamalat.co.id/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
# Display 
for each_ttl1 in soup.findAll('div',{'class':'jdl-feature-kurs color-corp'}):
    print (each_ttl1.text)    
for each_ttl2 in soup.findAll('div',{'class':'tgl-kurs color-corp'}):
    print (each_ttl2.text)        
print ("PT. Bank Muamalat, Tbk")       
# Populate data
for tr in soup.find_all('tr'): 
    cols = tr.find_all('td')
    tab.add_row([cols[0].text, cols[1].text, cols[2].text])
print (tab.draw())   
# Save to file (*csv)    
link1 = soup.find_all('tbody')
columns = soup.find_all('td')
dataset = [(x.text, y.text) for x,y in zip(link1, columns)]
with open("output.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in dataset[:50]: 
        writer.writerow(data)  