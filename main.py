from display import screen
import time
from maths import equations

########### VALUES ABLE TO BE CHANGED #######################
#x, y                                                       #
screen_size = [20, 10]                                      #   
                                                            #    
#Values for the object, mass is measured in kg              #    
#Also, if the object moves by one, it moves by 1 meter      #
mass = 4                                                    #
#M/s                                                        #        
starting_velocity = 0                                       #        
#X, y - initial position of the object                      #    
initial_position = [0, 5]                                   #
                                                            #
#Seconds/metre - 0.5 s/m = 2 ms                             #
sm = 0.5                                                    #
epochs = 60                                                 #            
#############################################################


final_pos = 0
direction = "right"
counter = 0
ms = 0

for i in range(0, epochs) :
    if direction == "right" :
        screen.draw_canvas(screen_size[0], screen_size[1], initial_position[0] + i, initial_position[1])
        print ("\nCurrent Velocity: " + str(equations.convert_sm_and_ms(sm)) + " m/s")
        time.sleep (sm)
    else :
        screen.draw_canvas(screen_size[0], screen_size[1], final_pos - counter, initial_position[1])

        #Uncomment the following line and comment the line after to allow the velocity to constantly increase over time
        #ms = ms + acceleration
        ms = acceleration
        print ("\nCurrent Velocity: " + str(ms) + " m/s")
        time.sleep (equations.convert_sm_and_ms(ms))

    if initial_position[0] + i == screen_size[0] :
        #Calculate force
        force = equations.calculate_acceleration(starting_velocity, equations.convert_sm_and_ms(sm), sm*i)
        acceleration = force * mass
        counter = 0
        direction = "left"
        final_pos =  initial_position[0] + i
    
    counter = counter + 1
    screen.clear()

