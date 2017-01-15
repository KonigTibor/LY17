"""Contains the landyacht module"""

from devices.devices import Controller, Servo, RotationSensor, Compass, GPS, Speedometer

from .messages import ControlMessageType
from .messages import MonitorMessageType, MonitorMessage

def landyacht(control_queue, monitor_queue):
    """Implements the landyacht module"""

    # Create a controller
    controller = Controller()

    # Create the devices attached to the land yacht
    steering_wheel = Servo(controller)
    sail = Servo(controller)
    vane = RotationSensor(controller)
    compass = Compass(controller)
    gps = GPS(controller)
    speedometer = Speedometer(controller)

    # Wait for messages from the control queue
    while True:

        # Get the next message from the control queue
        control_message = control_queue.get()

        # Process the message
        if control_message.message_type == ControlMessageType.TEST_LANDYACHT:
            # Test the land yacht
            # TODO: implement self-testing
            pass

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_STATUS:
            # Get the current status of the land yacht
            steering_wheel_angle = steering_wheel.get_angle()
            sail_angle = sail.get_angle()
            wind_direction = vane.get_direction()
            landyacht_direction = compass.get_direction()
            landyacht_position_x = gps.get_position_x()
            landyacht_position_y = gps.get_position_y()
            landyacht_speed = speedometer.get_speed()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_STATUS,
                steering_wheel_angle=steering_wheel_angle,
                sail_angle=sail_angle,
                wind_direction=wind_direction,
                landyacht_direction=landyacht_direction,
                landyacht_position_x=landyacht_position_x,
                landyacht_position_y=landyacht_position_y,
                landyacht_speed=landyacht_speed)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.TURN_STEERING_WHEEL:
            # Turn the steering wheel by the angle specified
            steering_wheel.turn(control_message.angle)

        elif control_message.message_type == ControlMessageType.TURN_SAIL:
            # Turn the sail by the angle specified
            sail.turn(control_message.angle)

        elif control_message.message_type == ControlMessageType.STOP_LANDYACHT:
            # Exit the loop and let the thread stop
            break
