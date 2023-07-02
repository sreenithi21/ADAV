import xml.etree.ElementTree as ET

# Parse the XML
tree = ET.parse('your_file.xml')
root = tree.getroot()

# Dictionary to store the distances
distances = {}

# Iterate over the vehicles
for vehicle in root.findall('vehicle'):
    vehicle_id = vehicle.get('id')
    route_id = vehicle.get('route')

    # Find the current vehicle's route
    route = root.find(f"route[@id='{route_id}']")
    edges = route.get('edges').split()

    # Find the index of the current vehicle's ID in the route edges
    vehicle_index = edges.index(vehicle_id)

    # Retrieve the preceding and succeeding vehicle IDs
    preceding_vehicle_id = edges[vehicle_index - 1] if vehicle_index > 0 else None
    succeeding_vehicle_id = edges[vehicle_index + 1] if vehicle_index < len(edges) - 1 else None

    # Store the distances in the dictionary
    distances[vehicle_id] = {
        'preceding': preceding_vehicle_id,
        'succeeding': succeeding_vehicle_id
    }

# Print the distances
for vehicle_id, distance in distances.items():
    print(f"Vehicle ID: {vehicle_id}")
    print(f"Preceding vehicle: {distance['preceding']}")
    print(f"Succeeding vehicle: {distance['succeeding']}")
    print()