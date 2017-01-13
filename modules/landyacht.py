"""Contains the landyacht module"""

from .messages import ControlMessageType
from .messages import MonitorMessageType, MonitorMessage

def landyacht(control_queue, monitor_queue):
    """Implements the landyacht module"""

    # TODO: create controllers and devices

    # Wait for messages from the control queue
    while True:

        # Get the next message from the control queue
        control_message = control_queue.get()

        # Process the message
        if control_message.message_type == ControlMessageType.TEST_LANDYACHT:
            # Test the land yacht
            # HACK: do nothing
            pass

        elif control_message.message_type == ControlMessageType.GET_STEERING_WHEEL_ANGLE:
            # Get the current angle of the steering wheel
            # HACK: return a constant
            angle = 201
            # Create a monitor message and put it into the monitor queue
            monitor_message = MonitorMessage(
                MonitorMessageType.STEERING_WHEEL_ANGLE,
                angle=angle)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_SAIL_ANGLE:
            # Get the current angle of the sail
            # HACK: return a constant
            angle = 202
            monitor_message = MonitorMessage(
                MonitorMessageType.SAIL_ANGLE,
                angle=angle)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_WIND_DIRECTION:
            # Get the current direction of the wind
            # HACK: return a constant
            direction = 203
            monitor_message = MonitorMessage(
                MonitorMessageType.WIND_DIRECTION,
                direction=direction)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_DIRECTION:
            # Get the current direction of the land yacht
            # HACK: return a constant
            direction = 204
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_DIRECTION,
                direction=direction)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.GET_LANDYACHT_POSITION:
            # Get the current position of the land yacht
            # HACK: return a constant
            position_x = 205
            position_y = 205
            monitor_message = MonitorMessage(
                MonitorMessageType.LANDYACHT_POSITION,
                position_x=position_x,
                position_y=position_y)
            monitor_queue.put(monitor_message)

        elif control_message.message_type == ControlMessageType.TURN_STEERING_WHEEL:
            # Turn the steering wheel by the angle specified
            angle = control_message.angle
            # HACK: do nothing

        elif control_message.message_type == ControlMessageType.TURN_SAIL:
            # Turn the sail by the angle specified
            angle = control_message.angle
            # HACK: do nothing

        elif control_message.message_type == ControlMessageType.STOP_LANDYACHT:
            # Exit the loop and let the thread stop
            break
