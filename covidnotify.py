from plyer import notification

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def notifyMe(title,message):
	notification.notify(title=title,message=message,app_icon='C://Users//Tanisha Goel//Desktop//notification//covid-ico.ico',timeout=10)

def getdata(url):
	content=requests.get(url)
	return content.text

if __name__=='__main__':
	##notifyMe("harry","let stop")
	data=getdata("https://www.mohfw.gov.in/")
	soup=BeautifulSoup(data,'html')
	list=soup.find_all("table")
	data=list[0].text.split('\n\n')
	states=["Haryana",'Rajasthan','Delhi']
	for item in data:
	    if item=='':
	        continue
	    else:
	       	final=item.split('\n')[1:]
	       	if final[1] in states:
	       		print(final)
	       		nTitle="Cases of Covid-19"
	       		nText=f"Name of States : {final[1]}\n Total conformed cases : {final[2]}\n Cured/Discharged : {final[3]}\n Deaths : {final[4]}"
	       		notifyMe(nTitle,nText)


