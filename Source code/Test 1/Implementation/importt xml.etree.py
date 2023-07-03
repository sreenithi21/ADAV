import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse(r"D:\desk top files 23\SREENITHI.R\NGN\PHASE - II\SUMO CODE\Implementation\Demo.rou.xml")
root = tree.getroot()

# Iterate over each vehicle element
for vehicle_elem in root.iter('vehicle'):
    vehicle_id = vehicle_elem.get('id')
    route_id = vehicle_elem.get('route')

    # Find the preceding and succeeding vehicle distances
    preceding_distance = None
    succeeding_distance = None

    for vehicle_elem2 in root.iter('vehicle'):
        if vehicle_elem2.get('id') != vehicle_id and vehicle_elem2.get('route') == route_id:
            # Preceding vehicle
            preceding_distance = vehicle_elem2.get('id')
            break

    for vehicle_elem3 in reversed(list(root.iter('vehicle'))):
        if vehicle_elem3.get('id') != vehicle_id and vehicle_elem3.get('route') == route_id:
            # Succeeding vehicle
            succeeding_distance = vehicle_elem3.get('id')
            break

    # Output the results
    print(f"Vehicle ID: {vehicle_id}")
    print(f"Route ID: {route_id}")
    print(f"Preceding Vehicle Distance: {preceding_distance}")
    print(f"Succeeding Vehicle Distance: {succeeding_distance}")
    print()