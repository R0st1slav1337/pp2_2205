import json

# Load the JSON data from the file
with open('c:/Users/rasti/Desktop/pp2_2025/week4/sample-data.json', 'r') as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 87)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 87)

# Iterate over the data and print the required fields
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")