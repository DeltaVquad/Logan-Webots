"""motor_test controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
def init_motors(motors_name):
    motors = []
    for m in motors_name:
        motors.append(robot.getDevice(m))
        motors[-1].setPosition(float('inf'))
        motors[-1].setVelocity(1.)
    return motors

motors = init_motors(['motor1', 'motor2', 'motor3', 'motor4'])
fix_vel = 100

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    motors[0].setVelocity(fix_vel)
    motors[1].setVelocity(-fix_vel)
    motors[2].setVelocity(fix_vel)
    motors[3].setVelocity(-fix_vel)

# Enter here exit cleanup code.
