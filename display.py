import os

class screen :
    def clear () :
        for i in range (0, os.get_terminal_size()[1]) :
            print ("")

    def draw_canvas (x, y, ball_x, ball_y) :
        #Draw top border
        for i in range(0, x) :
            print ("-", end = "")
        
        #Draw middle with border on edges
        for i in range(0, y) :
            print ("\n-", end = "")
            for b in range(0, x) :
                if b == ball_x and i == ball_y :
                    print ("B", end = "")
                else :
                    print (" ", end = "")
            print ("-", end = "")
        
        #Draw bottom border
        print ("")
        for i in range(0, x) :
            print ("-", end = "")