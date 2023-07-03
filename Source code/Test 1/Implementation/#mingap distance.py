import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse(r"D:\desk top files 23\SREENITHI.R\NGN\PHASE - II\SUMO CODE\Implementation\Demo.rou.xml")
root = tree.getroot()

# Iterate over the vehicles
for vehicle in root.iter('vehicle'):
    vehicle_id = vehicle.attrib['id']
    vehicle_type = vehicle.attrib['type']
    route = vehicle.attrib['route']

    # Find the preceding and succeeding vehicles
    preceding_vehicle = None
    succeeding_vehicle = None

    for preceding in vehicle.iter('vehicle'):
        if preceding.attrib['id'] != vehicle_id:
            preceding_vehicle = preceding
            break

    for succeeding in reversed(list(vehicle.iter('vehicle'))):
        if succeeding.attrib['id'] != vehicle_id:
            succeeding_vehicle = succeeding
            break

    # Get the distances to the preceding and succeeding vehicles
    preceding_distance = preceding_vehicle.attrib['depart'] if preceding_vehicle is not None else 'N/A'
    succeeding_distance = succeeding_vehicle.attrib['depart'] if succeeding_vehicle is not None else 'N/A'

    # Output the results
    print(f"Vehicle ID: {vehicle_id}")
    print(f"Type: {vehicle_type}")
    print(f"Route: {route}")
    print(f"Preceding Vehicle Distance: {preceding_distance}")
    print(f"Succeeding Vehicle Distance: {succeeding_distance}")
    print("")


