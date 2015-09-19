'''
Test Program for CMDmodule.
'''

#from CMDmodule import *
import CMDmodule as CMD
CMD = CMD.CMDmodule()
##def pwm_formula_test():
##    global a
##    PWM = 255
##    a = PWM*a
##    a = round(a, 1)
##    motor_a = a

while True:
    a = input("Change this value Test: ")
    CMD.pwm_formula_test()
    print a
