import os
import sys
import traci

# Set the path to the SUMO tools directory
sumo_tools_dir = "/path/to/sumo/tools"
sys.path.append(sumo_tools_dir)

# Connect to the SUMO server
traci.start(["sumo", "-c", "path/to/your/sumo_config_file.sumocfg"])

# Define the ID of the current vehicle
current_vehicle_id = "vehicle_0"

while traci.simulation.getMinExpectedNumber() > 0:
    # Get the position of the current vehicle
    current_vehicle_position = traci.vehicle.getPosition(current_vehicle_id)

    # Get the ID of the preceding vehicle
    preceding_vehicle_id = traci.vehicle.getLeader(current_vehicle_id)

    # Get the ID of the succeeding vehicle
    succeeding_vehicle_id = traci.vehicle.getFollower(current_vehicle_id)

    if preceding_vehicle_id == '':
        preceding_distance = float('inf')
    else:
        # Get the position of the preceding vehicle
        preceding_vehicle_position = traci.vehicle.getPosition(preceding_vehicle_id)

        # Calculate the distance between the current and preceding vehicles
        preceding_distance = traci.simulation.getDistance2D(current_vehicle_position[0], current_vehicle_position[1],
                                                           preceding_vehicle_position[0], preceding_vehicle_position[1])

    if succeeding_vehicle_id == '':
        succeeding_distance = float('inf')
    else:
        # Get the position of the succeeding vehicle
        succeeding_vehicle_position = traci.vehicle.getPosition(succeeding_vehicle_id)

        # Calculate the distance between the current and succeeding vehicles
        succeeding_distance = traci.simulation.getDistance2D(current_vehicle_position[0], current_vehicle_position[1],
                                                            succeeding_vehicle_position[0], succeeding_vehicle_position[1])

    print("Preceding distance:", preceding_distance)
    print("Succeeding distance:", succeeding_distance)

    # Advance the simulation by one step
    traci.simulationStep()

# Disconnect from the SUMO server
traci.close()