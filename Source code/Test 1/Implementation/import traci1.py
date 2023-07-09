import traci

def get_minimum_gaps():
    traci.start(['sumo-gui', '-c', r'D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg'])
    try:
    # Start the SUMO simulation and connect to TraCI
        simulation_duration = 10000  # in simulation steps
        for step in range(simulation_duration):
        # Perform simulation steps and TraCI actions
            traci.simulationStep()
        
        # Retrieve a list of all vehicle IDs
            vehicle_ids = traci.vehicle.getIDList()
            
            # Iterate over each vehicle and retrieve its preceding and succeeding vehicle IDs
            for vehicle_id in vehicle_ids:
                # Get the preceding vehicle ID
                preceding_vehicle_id = traci.vehicle.getLeader(vehicle_id)
                
                # Get the succeeding vehicle ID
                succeeding_vehicle_id = traci.vehicle.getFollower(vehicle_id)
                
                # Get the minimum gap distance with the preceding vehicle
                if preceding_vehicle_id != '':
                    minimum_gap_preceding = traci.vehicle.getMinGap(vehicle_id)
                else:
                    minimum_gap_preceding = None
                
                # Get the minimum gap distance with the succeeding vehicle
                if succeeding_vehicle_id != '':
                    minimum_gap_succeeding = traci.vehicle.getMinGap(vehicle_id)
                else:
                    minimum_gap_succeeding = None
                
                # Print the minimum gap distances
                print("Vehicle ID:", vehicle_id)
                print("Preceding Vehicle ID:", preceding_vehicle_id)
                print("Minimum Gap with Preceding Vehicle:", minimum_gap_preceding)
                print("Succeeding Vehicle ID:", succeeding_vehicle_id)
                print("Minimum Gap with Succeeding Vehicle:", minimum_gap_succeeding)
                print("-------------------------")
    except traci.TraCIException as e:
    # Handle TraCI exceptions, if necessary
        print("TraCI Error:", e)
    finally:
    # Stop the simulation and close the TraCI connection
        traci.close()

# Call the function to retrieve the minimum gap distances
get_minimum_gaps()