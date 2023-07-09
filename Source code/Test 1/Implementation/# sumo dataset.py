# sumo dataset
import os
import sys
import traci
import sumolib

sumo_tools_path = "C:/Program Files (x86)/Eclipse/Sumo/tools"
sys.path.append(sumo_tools_path)

sumo_binary = "sumo"  # or specify the path to the SUMO binary
sumo_config = r"D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg"
sumo_cmd = [sumo_binary, "-c", sumo_config]
traci.start(sumo_cmd)

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    # Retrieve and process lane data
    for lane_id in traci.lane.getIDList():
        lane_length = traci.lane.getLength(lane_id)
        lane_speed = traci.lane.getMaxSpeed(lane_id)
        lane_occupancy = traci.lane.getLastStepOccupancy(lane_id)
        lane_waiting_vehicles = traci.lane.getLastStepHaltingNumber(lane_id)
        lane_vehicle_count = traci.lane.getLastStepVehicleNumber(lane_id)
        # Process and store the lane data as needed

    # Retrieve and process vehicle data
    for vehicle_id in traci.vehicle.getIDList():
        vehicle_speed = traci.vehicle.getSpeed(vehicle_id)
        vehicle_lane = traci.vehicle.getLaneID(vehicle_id)
        vehicle_position = traci.vehicle.getPosition(vehicle_id)
        vehicle_acceleration = traci.vehicle.getAcceleration(vehicle_id)
        vehicle_waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
        # Process and store the vehicle data as needed

traci.close()
