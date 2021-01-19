# This hardware definition is used to control the hardware for a social decision making task
# as well as for the individual training of both types of animals (decision maker and recipient of the choice).
# Poke1 is a class using DIO_A for input and POW_A for LED, Poke2 is a class using DIO_B for input and POW_B for LED
from devices import *

# Instantiate Breakout board
board = Breakout_1_2()

# Instantiate Port Expander
port_exp = Port_expander(board.port_3)

# Instantiate motors
motor_1A  = Stepper_motor(board.port_1)  #Stepper motor controlling pellet delivery in reward area 1A
motor_1B  = Stepper_motor(board.port_2)  #Stepper motor controlling pellet delivery in reward area 1B
motor_2A  = Stepper_motor(board.port_4)  #Stepper motor controlling pellet delivery in reward area 2A
motor_2B  = Stepper_motor(board.port_5)  #Stepper motor controlling pellet delivery in reward area 2B

# Instantiate pokes for decision and food-seeking behaviour
poke_1A = Poke1(port_exp.port_1, rising_event = 'poke_1A', falling_event = 'poke_1A_out')  #Pokes for detecting decision to access reward area 1A
poke_1B = Poke2(port_exp.port_1, rising_event = 'poke_1B', falling_event = 'poke_1B_out')  #Pokes for detecting decision to access reward area 1B
poke_2A = Poke1(port_exp.port_2, rising_event = 'poke_2A', falling_event = 'poke_2A_out')  #Pokes for detecting decision to access reward area 2A
poke_2B = Poke2(port_exp.port_2, rising_event = 'poke_2B', falling_event = 'poke_2B_out')  #Pokes for detecting decision to access reward area 2B

# Instantiate IR detectors
IR_1A   = Poke1(port_exp.port_3, rising_event = 'IR_1A'  , falling_event = 'IR_1A_out' )  # IR detector in reward area 1A
IR_1B   = Poke2(port_exp.port_3, rising_event = 'IR_1B'  , falling_event = 'IR_1B_out' )  # IR detector in choice area 1
IR_1C   = Poke1(port_exp.port_4, rising_event = 'IR_1C'  , falling_event = 'IR_1C_out' )  # IR detector in reward area 1B
IR_2A   = Poke2(port_exp.port_4, rising_event = 'IR_2A'  , falling_event = 'IR_2A_out' )  # IR detector in reward area 2A
IR_2B   = Poke1(port_exp.port_5, rising_event = 'IR_2B'  , falling_event = 'IR_2B_out' )  # IR detector in choice area 2
IR_2C   = Poke2(port_exp.port_5, rising_event = 'IR_2C'  , falling_event = 'IR_2C_out' )  # IR detector in reward area 2B

# Instantiate feeders
feeder_1A   = Poke1(port_exp.port_6, rising_event = 'feeder_1A'  , falling_event = 'feeder_1A_out' )  #IR to detect pellet and retrieval in reward area 1A 
feeder_1B   = Poke2(port_exp.port_6, rising_event = 'feeder_1B'  , falling_event = 'feeder_1B_out' )  #IR to detect pellet and retrieval in reward area 1B
feeder_2A   = Poke1(port_exp.port_7, rising_event = 'feeder_2A'  , falling_event = 'feeder_2A_out' )  #IR to detect pellet and retrieval in reward area 2A
feeder_2B   = Poke2(port_exp.port_7, rising_event = 'feeder_2B'  , falling_event = 'feeder_2B_out' )  #IR to detect pellet and retrieval in reward area 2B

# Instantiate doors (digital outputs)
door_1A = Digital_output(pin = board.port_6.POW_A)     # Digital output to control opening and closening of pneumatic doors in reward area 1A
door_1B = Digital_output(pin = board.port_6.POW_B)     # Digital output to control opening and closening of pneumatic doors in reward area 1B
door_2A = Digital_output(pin = port_exp.port_8.POW_A)  # Digital output to control opening and closening of pneumatic doors in reward area 2A
door_2B = Digital_output(pin = port_exp.port_8.POW_B)  # Digital output to control opening and closening of pneumatic doors in reward area 2B
