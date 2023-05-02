import requests
from bs4 import BeautifulSoup as soup
from csv import DictWriter
from datetime import datetime
import time
while True:
    source = requests.get('http://192.168.137.98/')
    webpage= soup(source.content,features="html.parser")
    a1 = webpage.findAll('strong')

    esp = str(a1[0]).replace('<strong>','')
    esp=esp.replace('degree C.</strong>','')



    k = str(a1[1])
    k=k.replace('<strong>','')
    k=k.replace('degree C.</strong>','')
    p = str(a1[2])
    p=p.replace('<strong>','')
    p=p.replace('%.</strong>','')
    esp=int(esp)
    temp =int(k)
    hum= int(p)

    source2 = requests.get('http://192.168.137.242/')
    webpage2= soup(source2.content,features="html.parser")
    a2 = webpage2.findAll('strong')



    esp2 = str(a2[0]).replace('<strong>','')
    esp2=esp2.replace('degree C.</strong>','')
    k2 = str(a2[1])
    k2=k2.replace('<strong>','')
    k2=k2.replace('degree C.</strong>','')
    p2 = str(a2[2])
    p2=p2.replace('<strong>','')
    p2=p2.replace('%.</strong>','')
    esp2=int(esp2)
    temp2 =int(k2)
    hum2= int(p2)

    # k2 = str(a2[0])
    # k2=k2.replace('<strong>','')
    # k2=k2.replace('degree C.</strong>','')
    # p2 = str(a2[1])
    # p2=p2.replace('<strong>','')
    # p2=p2.replace('%.</strong>','')

    # temp2 =int(k2)
    # hum2= int(p2)



    now = datetime.now()
    field_names=['esp','Temp1','Humi1','Time1']
    List={'esp':esp,'Temp1':temp,'Humi1':hum,'Time1':now}
    with open('Book1.csv','a') as f_obj:
        dict_obj=DictWriter(f_obj,fieldnames=field_names)
        dict_obj.writerow(List)
        f_obj.close()
       



    

    
    field_names2=['esp2','Temp1','Humi1','Time1']
    List2={'esp2':esp2,'Temp1':temp2,'Humi1':hum2,'Time1':now}
    with open('Book1.csv','a') as f_obj:
        dict_obj=DictWriter(f_obj,fieldnames=field_names2)
        dict_obj.writerow(List2)
        f_obj.close()
    time.sleep(5)
       


