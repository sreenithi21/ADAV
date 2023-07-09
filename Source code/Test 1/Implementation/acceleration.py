import traci

def get_accelerations():
    traci.start(['sumo-gui', '-c', r'D:/desk top files 23/SREENITHI.R/NGN/PHASE - II/SUMO CODE/Implementation/myconfig.sumocfg'])
    try:
        # Start the SUMO simulation and connect to TraCI
        traci.simulationStep()  # Perform an initial simulation step to start the simulation
        
        while traci.simulation.getMinExpectedNumber() > 0:
            # Perform simulation steps and TraCI actions
            traci.simulationStep()
        
            # Retrieve a list of all vehicle IDs
            vehicle_ids = traci.vehicle.getIDList()
        
            # Iterate over each vehicle and retrieve its acceleration
            for vehicle_id in vehicle_ids:
                acceleration = traci.vehicle.getAcceleration(vehicle_id)
            
                # Print the acceleration of the vehicle
                print("Vehicle ID:", vehicle_id)
                print("Acceleration:", acceleration)
                print("-------------------------")
    
    except traci.TraCIException as e:
        # Handle TraCI exceptions, if necessary
        print("TraCI Error:", e)
    
    finally:
        # Stop the simulation and close the TraCI connection
        traci.close()

# Call the function to retrieve the accelerations
get_accelerations()
