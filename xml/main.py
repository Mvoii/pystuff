# https://docs.python.org/
import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# display classes and functions in ET module
# for (name, member) in getmembers(ET, isclass):
#     if not name.startswith("_"):
#         print(name)
# print("\nFunctions:")
# for (name, member) in getmembers(ET, isfunction):
#     if not name.startswith("_"):
#         print(name)


tree = ET.parse("pystuff/xml/holder.xml")# "holder.xml")
root = tree.getroot()
print(ET.tostring(root))

# get "coin" attribute
coin = root.get("coin")
print("Crypto name = {val}".format(val=coin))

# set "launched" attribute
root.set("launched", '20210101')
print(root.attrib)

# add id attribute to each investor
id = 1
for investor in tree.findall("investor"):
    investor.set("id", str(id))
    id += 1
    
# delete 'id' attributes
for investor in tree.findall("investor"):
    del(investor.attrib["id"])
    
# Add invetsor #1
# investor1 = ET.fromstring("<investor>Allen Duffy</investor>")
# root.append(investor1)

# Add investor #2
# investor2 = ET.Element("investor")
# investor2.text = "Karl Amber"
# root.append(investor2)
  
# add id once more
for (id, investor) in enumerate(root.findall("investor")):
    investor.set("id", str(id))

# select investor #4
investor = root.find(".//investor[@id='4']")
print(investor.text)


# save updated attribute
tree.write("pystuff/xml/holder.xml")
