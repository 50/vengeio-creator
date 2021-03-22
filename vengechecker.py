import requests
import json


def createAcc(username, password):
    success = False
    payload = "username="+username+"&"+"password="+password
    headers = {'Referer':'https://venge.io','Content-Type':'application/x-www-form-urlencoded'}
    req = requests.session()
    req.headers.update(headers)
    req1 = req.post("https://gateway.venge.io/?request=login",data=payload)
    if(json.loads(req1.text)['success'] == True):
        success = True
    return success    
ignlist = open("igns.txt","r").readlines()
password = input("Type password: ")
created = []
for x in ignlist:
    status = createAcc(x.replace("\n",""), password)
    if status == True:
        #print("[%s]Successfully Created" %(x))
        print(x.replace("\n","") + ":" + password)
        created.append(x + ":" + password)


