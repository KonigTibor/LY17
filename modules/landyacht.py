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

        elif control_message.message_type == ControlMessageType.GET_STEERING_WHEEL_ANGLE:
            # Get the current angle of the steering wheel
            angle = steering_wheel.get_angle()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.STEERING_WHEEL_ANGLE,
                angle=angle)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_SAIL_ANGLE:
            # Get the current angle of the sail
            angle = sail.get_angle()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.SAIL_ANGLE,
                angle=angle)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_WIND_DIRECTION:
            # Get the current direction of the wind from the vane
            direction = vane.get_direction()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.WIND_DIRECTION,
                direction=direction)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_DIRECTION:
            # Get the current direction of the land yacht from the compass
            direction = compass.get_direction()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_DIRECTION,
                direction=direction)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_POSITION:
            # Get the current position of the land yacht from the GPS
            position_x = gps.get_position_x()
            position_y = gps.get_position_y()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_POSITION,
                position_x=position_x,
                position_y=position_y)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_SPEED:
            # Get the current direction of the land yacht from the compass
            speed = speedometer.get_speed()
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_SPEED,
                speed=speed)
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
