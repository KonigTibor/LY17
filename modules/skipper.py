"""Contains the skipper module"""

from enum import Enum, auto

from .messages import CommandMessageType, CommandMessage
from .messages import ControlMessageType, ControlMessage

def skipper(command_queue, control_queue, monitor_queue):
    """Implements the skipper module"""

    # Display help
    display_help()

    # Wait for user input
    while True:

        # Ask for the user's selection
        choice = int(input("Enter the number of operation you selected: "))

        # Process the user's selection
        if choice == Operation.DISPLAY_HELP.value:
            # Display help
            display_help()

        elif choice == Operation.GET_STEERING_WHEEL_ANGLE.value:
            # Get the (relative) angle of the steering wheel
            # Create and send a GET_STEERING_WHEEL_ANGLE message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_STEERING_WHEEL_ANGLE)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Steering wheel angle: {} degrees".format(monitor_message.angle))

        elif choice == Operation.GET_SAIL_ANGLE.value:
            # Get the (relative) angle of the sail
            # Create and send a GET_SAIL_ANGLE message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_SAIL_ANGLE)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Sail angle: {} degrees".format(monitor_message.angle))

        elif choice == Operation.GET_WIND_DIRECTION.value:
            # Get the (relative) direction of the wind
            # Create and send a GET_WIND_DIRECTION message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_WIND_DIRECTION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Wind direction: {} degrees".format(monitor_message.direction))

        elif choice == Operation.GET_LANDYACHT_DIRECTION.value:
            # Get the (absolute) direction of the land yacht
            # Create and send a GET_LANDYACHT_DIRECTION message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_LANDYACHT_DIRECTION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Land yacht direction: {} degrees".format(monitor_message.direction))

        elif choice == Operation.GET_LANDYACHT_POSITION.value:
            # Get the (absolute) position of the land yacht
            # Create and send a GET_LANDYACHT_POSITION message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_LANDYACHT_POSITION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Land yacht position: {}, {}".format(monitor_message.position_x, monitor_message.position_y))

        elif choice == Operation.GET_LANDYACHT_SPEED.value:
            # Get the speed of the land yacht
            # Create and send a GET_LANDYACHT_SPEED message to the land yacht
            control_message = ControlMessage(ControlMessageType.GET_LANDYACHT_SPEED)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Land yacht speed: {}".format(monitor_message.speed))

        elif choice == Operation.TURN_STEERING_WHEEL.value:
            # Turn the steering wheel by the angle specified by the user
            angle = int(input("Enter the new angle: "))
            # Create and send a TURN_STEERING_WHEEL message to the land yacht
            control_message = ControlMessage(ControlMessageType.TURN_STEERING_WHEEL, angle=angle)
            control_queue.put(control_message)

        elif choice == Operation.TURN_SAIL.value:
            # Turn the sail by the angle specified by the user
            angle = int(input("Enter the new angle: "))
            # Create and send a TURN_SAIL message to the land yacht
            control_message = ControlMessage(ControlMessageType.TURN_SAIL, angle=angle)
            control_queue.put(control_message)

        elif choice == Operation.NAVIGATE_TO_DIRECTION.value:
            # Navigate to the direction specified by the user
            direction = int(input("Enter the new direction: "))
            # Create and send a NAVIGATE_TO_DIRECTION message to the AI
            command_message = CommandMessage(CommandMessageType.NAVIGATE_TO_DIRECTION, direction=direction)
            command_queue.put(command_message)

        elif choice == Operation.NAVIGATE_TO_POSITION.value:
            # Navigate to the position specified by the user
            position_x = int(input("Enter the X position: "))
            position_y = int(input("Enter the Y position: "))
            # Create and send a NAVIGATE_TO_POSITION message to the AI
            command_message = CommandMessage(CommandMessageType.NAVIGATE_TO_POSITION, position_x=position_x, position_y=position_y)
            command_queue.put(command_message)

        elif choice == Operation.STOP_LANDYACHT.value:
            # Stop the land yacht
            # Create and send a STOP_AI message to the AI
            command_message = CommandMessage(CommandMessageType.STOP_AI)
            command_queue.put(command_message)
            # Create and send a STOP_LANDYACHT message to the land yacht
            control_message = ControlMessage(ControlMessageType.STOP_LANDYACHT)
            control_queue.put(control_message)
            # Exit the loop and let the thread stop
            break

def display_help():
    """Displays the list of available operations"""
    print("Operations:")
    print("{} - Display help".format(Operation.DISPLAY_HELP.value))
    print("{} - Get the angle of the steering wheel".format(Operation.GET_STEERING_WHEEL_ANGLE.value))
    print("{} - Get the angle of the sail".format(Operation.GET_SAIL_ANGLE.value))
    print("{} - Get the direction of the wind".format(Operation.GET_WIND_DIRECTION.value))
    print("{} - Get the direction of the land yacht".format(Operation.GET_LANDYACHT_DIRECTION.value))
    print("{} - Get the position of the land yacht".format(Operation.GET_LANDYACHT_POSITION.value))
    print("{} - Get the speed of the land yacht".format(Operation.GET_LANDYACHT_SPEED.value))
    print("{} - Turn the steering wheel".format(Operation.TURN_STEERING_WHEEL.value))
    print("{} - Turn the sail".format(Operation.TURN_SAIL.value))
    print("{} - Navigate to direction".format(Operation.NAVIGATE_TO_DIRECTION.value))
    print("{} - Navigate to position".format(Operation.NAVIGATE_TO_POSITION.value))
    print("{} - Stop the land yacht".format(Operation.STOP_LANDYACHT.value))

class Operation(Enum):
    """Implements the Operation enumeration"""
    DISPLAY_HELP = 0
    GET_STEERING_WHEEL_ANGLE = auto()
    GET_SAIL_ANGLE = auto()
    GET_WIND_DIRECTION = auto()
    GET_LANDYACHT_DIRECTION = auto()
    GET_LANDYACHT_POSITION = auto()
    GET_LANDYACHT_SPEED = auto()
    TURN_STEERING_WHEEL = auto()
    TURN_SAIL = auto()
    NAVIGATE_TO_DIRECTION = auto()
    NAVIGATE_TO_POSITION = auto()
    STOP_LANDYACHT = 99
