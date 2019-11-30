import requests 
from bs4 import BeautifulSoup 
import csv 
visited=[]
link='https://urdu.arynews.tv/dr-arif-alvi-pak-afriqa-isb/'
with open('out.csv', 'w') as f: 
    w = csv.DictWriter(f,['srNo','label','link','news']) 
    w.writeheader() 
    i=0
    while i <= 200:
        i+=1
        if(link in visited):
            i-=1
            continue
        r = requests.get(link) 
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('article', attrs = {'class':'post'}) 
        obj={'srNo':i,'link':link,'news':''}
        visited.append(link)
        link = soup.find('a',attrs={'rel':'next'})['href']
        label = soup.find('li',attrs={'class':'current-post-ancestor'})
        if(label == None):
            print ('label not detected ', i)
            i-=1
            print (i)
            continue
        obj['label']=label.find('a').string
        for row in table.findAll('p'): 
            if(row.string !=None):
                obj['news'] = obj['news'] + row.string
        print(obj)
        w.writerow(obj) 
        print("////////////-------------")
