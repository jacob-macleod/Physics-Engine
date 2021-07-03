class equations :
    #Convert seconds per metre into metres per second and back gain
    def convert_sm_and_ms (speed) :
        return 1/speed

    #Calculate weight in N from mass
    def calculate_weight_from_mass (mass) :
        return mass * 3.34

    def calculate_acceleration (initial_velocity, final_velocity, time) :
        velocity = final_velocity - initial_velocity
        return velocity / time
