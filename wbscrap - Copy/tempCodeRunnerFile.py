import requests
from bs4 import BeautifulSoup as soup
from csv import DictWriter
from datetime import datetime
import time
while True:
    source = requests.get('http://192.168.137.158/')
    webpage= soup(source.content,features="html.parser")
    a1 = webpage.findAll('strong')

    k = str(a1[0])
    k=k.replace('<strong>','')
    k=k.replace('degree C.</strong>','')
    p = str(a1[1])
    p=p.replace('<strong>','')
    p=p.replace('%.</strong>','')

    temp =int(k)
    hum= int(p)








    now = datetime.now()

    
    field_names=['Temperature','Humidity','Time']
    List={'Temperature':temp,'Humidity':hum,'Time':now}
    with open('Book1.csv','a') as f_obj:
        dict_obj=DictWriter(f_obj,fieldnames=field_names)
        dict_obj.writerow(List)
        f_obj.close()
        time.sleep(5)


