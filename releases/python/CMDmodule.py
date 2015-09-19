# C:\python27\Lib

'''
Invert Code for Arduino PWM when Digital
Channel is 'LOW' along with a few other
bits and pieces.
'''
##set_zero = 0
##
##if set_zero == 0:
##    from set_zero import *
##    set_zero = set_zero + 1
##else:
##    print "Module set_zero imported!"
class CMDmodule():
    print "Welcome to CMDmodule.  Use Wisely. "

    def __init__(self, init=0, question_two=0, a=0, b=0, debug_value=0, motor_a_prev=0, motor_b_prev=0, dir_y_prev=0):
        self.init = init
        self.question_two = question_two
        self.a = a
        self.b = b
        self.debug_value = debug_value
        self.motor_a_prev = motor_a_prev
        self.motor_b_prev = motor_b_prev
        self.dir_y_prev = dir_y_prev
        print "Valables set to Zero!"

    def invert_y_axis(self, y):
        global y
        if y < 0:                  ############################
            return abs(y)          #New Y-axes inversion code!#
        elif y > 0:                ############################
            return y*-1

    def sendcommand(motor_a,motor_b,dir_y):
        byte1 = chr(int(motor_a))
        byte2 = chr(int(motor_b))
        byte3 = chr(int(dir_y))
        sock.send(byte1+byte2+byte3)


    def convert_pwm(self, a):
        return round(a*255,0)


    def arduino_direction(self, y):
        if y < 0:           
            return 2           
        else:               
            return 1

    def invert_motor(self, value):
        return 255 - value



        
