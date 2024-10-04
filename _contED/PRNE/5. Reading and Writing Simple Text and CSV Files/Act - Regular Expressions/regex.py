import re

names = ["Arthur James",
         "Edwin Inson",
         "Geir Anders Berge",
         "Finn Bindeballe",
         "HappyCodingRobot",
         "Ron Cromberge",
         "Sohil"
        ]

pattern = r"^\w\w\w\w\w\w\s"

#for name in names:
#   result = re.search(pattern, name)
#    print(result)

names2 = [
          "Brian Daugette",
          "Veronica Supersonice",
          "Tony Gasparovic",
          "Patrick Germann",
          "m!sha"
         ]   
regex = r"^(?P<fn>\w+)\s+(?P<ln>\w+)$"
regexOChar = r"^[a-zA-Z!]+$"

for name in names2:
    result = re.search(regexOChar, name)
    if result:    
        print(name)
        #print(result.group("fn"))
        #print(result.group("ln"))