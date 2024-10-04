import re

pattern = "GigabitEthernet[1-4]"
interface = "interface GigabitEthernet3 ip address 10.11.0.1 255.255.255.0"

pattern2 = "A.....s"
pattern3 = "GigabitEthernet[1-4]"
interface2 = "interface GigabitEthernet3 ip Address 10.11.0.1 255.255.255.0 GigabitEthernet4 GigabitEthernet2"
#result = re.search(pattern, interface)
result = re.search(pattern3, interface2)
resultall = re.findall(pattern3, interface2)
resultallS = re.split(pattern3, interface2)
print(resultallS)