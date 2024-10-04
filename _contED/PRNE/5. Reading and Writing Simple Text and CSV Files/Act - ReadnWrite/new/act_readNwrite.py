import csv

_data = [
           {
               "First Name" : "John",
               "Last Name" : "Doe",
               "Age" : "25",
               "Position" : "System Admin"
           },
           {
               "First Name" : "Abby",
               "Last Name" : "Smith",
               "Age" : "28",
               "Position" : "Full Stack Dev"
           },
           {
               "First Name" : "Ryan",
               "Last Name" : "Rochet",
               "Age" : "24",
               "Position" : "Creative Director"
           }
       ]

#For writing on .txt
#with open("writeInTXT.txt", "w") as file:
#    for i in range(0, 3):
#        file.write(str(_data[i]))
#        file.write("\n")
#print(_data[0]["Age"])

#For reading .txt
#with open("writeInTXT.txt", "r") as file:
#    Content = file.read()
#    print(Content)

#For writing on .csv
#with open("writeInCSV.csv", "w") as csvFile:
#    conv = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
#    for row in _data:
#        conv.writerow(row.items())
        
#For reading .csv
with open("writeInCSV.csv", "r") as csvFile:
    content = csvFile.read()
    print(content)
    