import csv
import os
import sys
import traci
import sumolib


# Start the SUMO simulation
sumo_tools_path = "C:/Program Files (x86)/Eclipse/Sumo/tools"
sys.path.append(sumo_tools_path)

sumo_binary = "sumo"  # or specify the path to the SUMO binary
sumo_config = "D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg"
sumo_cmd = [sumo_binary, "-c", sumo_config]
traci.start(sumo_cmd)



#Run the simulation for a specified number of steps
simulation_steps = 10000
for step in range(simulation_steps):
    traci.simulationStep()

# Retrieve vehicle information
vehicle_ids = traci.vehicle.getIDList()
vehicle_data = []
for vehicle_id in vehicle_ids:
    vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
    vehicle_route = traci.vehicle.getRouteID(vehicle_id)
    vehicle_data.append([vehicle_id, vehicle_speed, vehicle_route])

# Stop the SUMO simulation
# Store vehicle information in a CSV file
csv_file = "vehicle_data.csv"
csv_header = ["Vehicle ID", "Speed", "Route ID"]

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)
    writer.writerows(vehicle_data)

# Print a message to indicate the completion and location of the CSV file
print("Vehicle information saved to:", os.path.abspath(csv_file))

traci.close()























































































# import csv
# import os
# import sys
# import traci
# import sumolib

# # Set the SUMO tools path
# sumo_tools_path = "C:/Program Files (x86)/Eclipse/Sumo/tools"
# sys.path.append(sumo_tools_path)

# # Specify the SUMO binary and configuration file paths
# sumo_binary = "sumo"
# sumo_config = "D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg"

# # Start SUMO and TraCI
# sumo_cmd = [sumo_binary, "-c", sumo_config]
# traci.start(sumo_cmd)

# # Define output file path
# vehicle_data_file = "vehicle_data.csv"

# try:
#     # Retrieve and store vehicle data
#     vehicle_data = []
#     for vehicle_id in traci.vehicle.getIDList():
#         vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
#         vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
#         vehicle_position = traci.vehicle.getPosition(vehicle_id)
#         vehicle_acceleration = traci.vehicle.getAcceleration(vehicle_id)
#         vehicle_waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
        
#         # Append vehicle data to the list
#         vehicle_data.append([
#             vehicle_id,
#             str(vehicle_speed),
#             vehicle_lane,
#             str(vehicle_position[0]),
#             str(vehicle_position[1]),
#             str(vehicle_acceleration),
#             str(vehicle_waiting_time)
#         ])

#         # Print vehicle data
#         print("Vehicle ID:", vehicle_id)
#         print("Speed:", vehicle_speed)
#         print("Lane:", vehicle_lane)
#         print("Position X:", vehicle_position[0])
#         print("Position Y:", vehicle_position[1])
#         print("Acceleration:", vehicle_acceleration)
#         print("Waiting Time:", vehicle_waiting_time)
#         print("-------------------------")

#     # Write vehicle data to CSV file
#     with open(vehicle_data_file, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Vehicle ID", "Speed", "Lane", "Position X", "Position Y", "Acceleration", "Waiting Time"])
#         writer.writerows(vehicle_data)

# finally:
#     # Close the TraCI connection and stop the simulation
#     traci.close()