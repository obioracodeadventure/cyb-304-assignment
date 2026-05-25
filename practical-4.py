import xml.etree.ElementTree as ET

with open("students.xml", "r") as file:
    data = file.read()

# Parse XML string
root = ET.fromstring(data)
print(root.find('name').text) # Ada

# Real-world: Banking systems, enterprise apps