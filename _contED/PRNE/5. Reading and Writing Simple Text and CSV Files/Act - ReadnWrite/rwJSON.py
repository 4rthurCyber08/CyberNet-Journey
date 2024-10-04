import json

data = {
            "IP" : "192.168.1.3", 
            "MASK" : "255.255.255.192",
            "TYPE" : "IPV4", 
            "PROTOCOL" : "TCP/IP"
       }

dataL = [
          {
            "IP" : "192.168.1.3", 
            "MASK" : "255.255.255.192",
            "TYPE" : "IPV4", 
            "PROTOCOL" : "TCP/IP"
          },
          {
            "IP" : "10.10.20.40", 
            "MASK" : "255.255.255.252",
            "TYPE" : "IPV4", 
            "PROTOCOL" : "TCP/IP"
          }
        ]
        
with open ('newjsonfile.json', 'w') as file:
    count = 0
    for i in dataL:
       json.dump(dataL, file)
       json.dump("\n", file)
       count += 1