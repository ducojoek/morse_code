import time
from morse_code.arduino_controller import ArduinoVISADevice

lamp = ArduinoVISADevice(ports=)


def word():
    # functie ontvangt lichtsignalen en vertaalt deze naar dots(1), dash(2), en volgende letter(3).
    # en returned een lijst met 


    space = 0
    crucial_value = 0
    above_crucial_count = 0
    below_crucial_count = 0
    one_three = 0

    dot_len = 5
    dash_len = 10
    let_len = 30
    space_len = 60


    while space == 0:
        U = int(lamp.get_input_value(channel= 1)) - int(lamp.get_input_value(channel=2))

        if U > crucial_value:
            above_crucial_count += 1
            below_crucial_count = 0
            one_three = 0

        if U < crucial_value:
            below_crucial_count +=1

            if dot_len <= above_crucial_count >= dash_len:
                word += str(1)

            if above_crucial_count>= dash_len:
                word += str(2)

            if below_crucial_count >= let_len and one_three < 1:
                word += str(3)

            if below_crucial_count >= space_len:
                return word
            
            above_crucial_count = 0

        time.pause(0.01)


def translater():



    
            

            
            