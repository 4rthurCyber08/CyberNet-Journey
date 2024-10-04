import csv

_ip = "10.40.1.4"
_mask = "255.255.255.0"

data = [
            ['Hostname', 'Vendor', 'Model', 'Location'],
            ['sw10', 'Cisco', '3800', 'Miami'],
            ['sw11', 'Palo Alto', '3650', 'Atlanta']
       ]

txtData = "Switch1 is located in San Jose"

with open("switch.csv", "r") as file:
    content = file.readlines(50)
    
    print(content)

#with open("switch.txt", "a") as f:
    #f.write(txtData)
  
#    f.write("\n")
    
#    for i in range(0, 3):
#        f.write(str(data[i][i]))
#        f.write("\n")
    

#with open("switch.csv", "a") as f:
#    devices = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#    for row in data:
#        devices.writerow(row)
    
#with open("switch.txt") as f:
    