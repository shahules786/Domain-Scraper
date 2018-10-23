try:
   import random 
   import re
   import datetime
   from urllib.request import urlopen
   from bs4 import BeautifulSoup
except ImportError:
    print("import error")

pages=set()
random.seed(datetime.datetime.now())
def getInternalLinks(bsobj,includeurl):
    internalLinks=[]
    for links in bsobj.findAll("a",{"href":re.compile("^(/|.*"+includeUrl+")")}):
        if links.attrs['href'] is not None:
            if links.attrs["href"]  not in internalLinks:
               internalLinks.append(links.attrs['href'])
    return(internalLinks)
def getExternallinks(bsobj,excludeUrl):
    ExternalLinks=[]
    for links in bsobj.findAll('a',href=re.compile(("^(http|www)((?!"+excludeUrl+").)*$"))):
       if links.attrs['href'] is not None:
          if links.attrs["href"] not in ExternalLinks:
             ExternalLinks.append(links.attrs["href"])
    return(ExternalLinks)

def splitaddress(address):
               return(address.replace("http://"," ").split("/"))
def getrandomexternal(startingpage):
   html=urlopen(startingpage)
   bsobj=BeautifulSoup(html,"html.parser")
   externallinks=getExternallinks(bsobj,splitaddress(startingpage)[0])
   if externallinks ==0:
      internallinks=getInternalLinks(bsobj,startingpage)
      return (getExternalLinks(internallinks[random.randint(0,len(internallinks)-1)]))
   else:
      return externallinks[random.randint(0 ,len(externallinks)-1)]


                              
def followlinks(startingpage):
            externallinks=getrandomexternal(startingpage)
            print("external link :"+externallinks)
            followlinks(externallinks)
followlinks("http://oreilly5.com")                              
