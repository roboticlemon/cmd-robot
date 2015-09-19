
print "Welcome to Servo testing Script!"

while True:
    x = input("Input 'x' value between 0 - 1: ")
    servo_turn = 90 + (45*x)
    servo_turn = round(servo_turn, 0)
    print servo_turn
