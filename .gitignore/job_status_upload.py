# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:18:03 2017

@author: pvangala
"""
import smtplib
import requests
from email.mime.text import MIMEText

#enter node ip here and job id you want to get information about
url = "https://nodeip:8080/platform/1/job/jobs/job_id"

#modify your credentials, you can use postman to get the headers or you can create your own header
headers = {
    'authorization': "Basic enter credentials",
    'cache-control': "no-cache",
    'postman-token': "you can find token in postman"
    }

response = requests.request("GET", url, headers=headers,verify=False).json()
job_state=response['jobs'][0]['state']
server=smtplib.SMTP('enter your mail server details here')
msg=MIMEText('Job is complete')
test=msg.as_string()

if job_state=='succeeded':
    server.sendmail('from email address', 'to email address', test)