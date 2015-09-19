import pygame
from time import sleep
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print j.get_name()
if j.get_name() == 'wide':
    print 'axis(0) is controlled by RIGHT-SIDE / FORWARDS --> BACKWARDS (Vertical)'
    print 'axis(1) is controlled by RIGHT-SIDE / LEFT --> RIGHT (Horizontal)'
    print 'axis(2) is controlled by LEFT-SIDE / FORWARDS --> BACKWARDS (Vertical)'
    print 'axis(3) is UNKNOWN*      *AFFECTTED by RIGHT-SIDE / Vertical movement'
    print 'axis(4) is UNKNOWN'
    print 'axis(5) is controlled by LEFT-SIDE / LEFT --> RIGHT (Horizontal)'

sleep(1)
i = raw_input('Which side of the Remote do you want to use? (right / left / all / both / button): ')
pygame.event.pump()
while i == 'right':
    pygame.event.pump()
    w = j.get_axis(0)*100
    w = round(w,11)
    w = int(w)
    x = j.get_axis(1)*100
    x = round(x,11)
    x = int(x)
    print 'Horizontal: '+ str(x)+ '  '+ 'Vertical: '+ str(w)
while i == 'left':
    pygame.event.pump()
    y = j.get_axis(2)*100
    y = round(y,11)
    y = int(y)
    b = j.get_axis(5)*100
    b = round(b,11)
    b = int(b)
    print 'Horizontal: '+ str(b)+ '  '+ 'Vertical: '+ str(y)
 
while i == 'both':
    pygame.event.pump()
    w = j.get_axis(0)*100
    w = round(w,11)
    w = int(w)
    x = j.get_axis(1)*100
    x = round(x,11)
    x = int(x)
    y = j.get_axis(2)*100
    y = round(y,11)
    y = int(y)
    b = j.get_axis(5)*100
    b = round(b,11)
    b = int(b)
    print 'Right Stick: '+'Horizontal: '+ str(x)+ '  '+ 'Vertical: '+ str(w)+ '                               Left Stick: '+'Horizontal: '+ str(b)+ '  '+ 'Vertical: '+ str(y)

while i == 'all':
    pygame.event.pump()
    w = j.get_axis(0)*1
    w = round(w,2)
    x = j.get_axis(1)*1
    x = round(x,2)
    y = j.get_axis(2)*1
    y = round(y,2)
    z = j.get_axis(3)*1
    z = round(z,2)
    a = j.get_axis(4)*1
    a = round(a,2)
    b = j.get_axis(5)*1
    b = round(b,2)
    #print (w, x, y, z, a, b)
    print str(w) + '   ' + str(x) + '   ' + str(y) + '   ' + str(z) + '   ' + str(a) + '   ' + str(b)
               
while i == 'button':
    if j.get_name() == 'wide':
        print 'No buttons on this remote!'
        break
    else:
        if j.get_button(0):
            print "Button 0 pressed"
        if j.get_button(1):
            print "Button 1 pressed"
        if j.get_button(2):
            print "Button 2 pressed"
        if j.get_button(3):
            print "Button 2 pressed"
        if j.get_button(4):
            print "Button 4 pressed"
        if j.get_button(5):
            print "Button 5 pressed"
        if j.get_button(6):
            print "Button 6 pressed"
        if j.get_button(7):
            print "Button 7 pressed"
        if j.get_button(8):
            print "Button 8 pressed"
        if j.get_button(7):
            print "Button 7 pressed"

while i == 'debug':
    pygame.event.pump()
    z = j.get_axis(3)*100
    z = round(z,2)
    #z = int(z)
    a = j.get_axis(4)*100
    a = round(a,2)
    #z = int(a)
    print str(z) + '       ' + str(a) 
    
