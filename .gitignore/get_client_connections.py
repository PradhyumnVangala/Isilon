# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 07:58:26 2017

@author: pvangala
"""
# this would return a variable with all client names if they are found in nslookup else will be added via ip
import requests
import socket
userid='username'
password='password'
Node_ips=['add all node ip's here']
#this would be a client connection per node function
def get_smb_sessions_pernode(userid,password,url):
    smb_sessions=requests.get(url,auth=(userid,password),verify=False).json()
    node1_sessions=smb_sessions['sessions']
    clients=[]
    for i in range(len(node1_sessions)):
        clients.insert(0,node1_sessions[i]['computer'])
    return clients

    
#To loop through all the nodes use this loop
#Node_ips=[ ]
#add ip's of nodes you want to get the client connections
Node_ips=['add all node ip's here']
for i in Node_ips:
    url='https://'+i+':8080/platform/1/protocols/smb/sessions'
    print (url)
    all_node_ip_connections.insert(0,get_smb_sessions_pernode(userid,password,url))

all_client_names=[]
for i in range(len(all_node_ip_connections)):
    per_node_ip_connections=all_node_ip_connections[i]
    for i in per_node_ip_connections:
        
        try:
            client_ip=socket.gethostbyaddr(i)
            all_client_names.insert(0,client_ip[0])
        except socket.herror:
            all_client_names.insert(0,i)
        