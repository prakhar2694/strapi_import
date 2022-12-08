import os,pandas as pd,json
os.chdir('Downloads')

df = pd.read_csv('talentserve.xlsx - Sheet2 (1).csv',skiprows=9836,nrows=50000)
import requests

import uuid

import json
#import random
#for ind in df.index
for ind in df.index:
    
    

    url = "https://datastore.amoga.app/talentserve/api/studentdetails"

    randomFun= str(uuid.uuid1())
    payload = json.dumps({

      "data": {

        "name": df['ANJUM FATHIMA'][ind],
        "city": df['HYDERABAD'][ind],
        "mobileno":str(df['9989276438'][ind]),
        "email":df['aktherm.22@gmail.com'][ind],
        "assignee":"rahul@talentserve.org",
        "status":"new",
        "task_type":"studentdetail",
        "priority":"medium",
        "amo_application_id":"7f44a3a5-ad6d-4e45-9c3d-5a42043bbfe3",
        "workflow_id":randomFun,
        "workflow_instance_id":randomFun
      }

    })

    headers = {

      'Authorization': 'Bearer 7ddf635541978cca1073c63ad3bc05bc349327b67167d31a056ac553be33f16169f7c1fc9ccdda795a63e58136d0f00c44133a5284eea4cd666a66fe1cfc2dfc71d77fe63507ce5f48c10d34637b6f14464203e23f9d034cac3475bb8aef9b86cfba472a89a891d7dea205a882a8870077ce4985e04947f8ab9f7f01f3e946dd',

      'Content-Type': 'application/json'

    }


    #print(randomFun,payload)
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)



print(response.text)