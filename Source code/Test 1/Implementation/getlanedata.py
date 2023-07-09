import csv
import os
import sys
import traci
import sumolib

sumo_tools_path = "C:/Program Files (x86)/Eclipse/Sumo/tools"
sys.path.append(sumo_tools_path)

sumo_binary = "sumo"  # or specify the path to the SUMO binary
sumo_config = "D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg"
sumo_cmd = [sumo_binary, "-c", sumo_config]
traci.start(sumo_cmd)

# Define output file paths
lane_data_file = "lane_data.csv"

#Retrieve and store lane data
lane_data = []
for lane_id in traci.lane.getIDList():
    lane_length = traci.lane.getLength(lane_id)
    lane_speed = traci.lane.getMaxSpeed(lane_id)
    lane_occupancy = traci.lane.getLastStepOccupancy(lane_id)
    lane_waiting_vehicles = traci.lane.getLastStepHaltingNumber(lane_id)
    lane_vehicle_count = traci.lane.getLastStepVehicleNumber(lane_id)
    
    # Append lane data to the list
    lane_data.append([
        lane_id,
        lane_length,
        lane_speed,
        lane_occupancy,
        lane_waiting_vehicles,
        lane_vehicle_count
    ])

    # Print lane data
    print("Lane ID:", lane_id)
    print("Length:", lane_length)
    print("Speed:", lane_speed)
    print("Occupancy:", lane_occupancy)
    print("Waiting Vehicles:", lane_waiting_vehicles)
    print("Vehicle Count:", lane_vehicle_count)
    print("-------------------------")

# Retrieve and store vehicle data

#Write lane data to CSV file
with open(lane_data_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Lane ID", "Length", "Speed", "Occupancy", "Waiting Vehicles", "Vehicle Count"])
    writer.writerows(lane_data)

traci.close()
