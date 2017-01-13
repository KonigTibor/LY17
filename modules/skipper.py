"""Contains the skipper module"""

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
        if choice == 0:
            # Display help
            display_help()

        elif choice == 1:
            # Get the (relative) angle of the steering wheel
            # Create and send a GET_STEERING_WHEEL_ANGLE message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.GET_STEERING_WHEEL_ANGLE)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Steering wheel angle: {} degrees".format(
                monitor_message.angle))

        elif choice == 2:
            # Get the (relative) angle of the sail
            # Create and send a GET_SAIL_ANGLE message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.GET_SAIL_ANGLE)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Sail angle: {} degrees".format(
                monitor_message.angle))

        elif choice == 3:
            # Get the (relative) direction of the wind
            # Create and send a GET_WIND_DIRECTION message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.GET_WIND_DIRECTION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Wind direction: {} degrees".format(
                monitor_message.direction))

        elif choice == 4:
            # Get the (absolute) direction of the land yacht
            # Create and send a GET_LANDYACHT_DIRECTION message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.GET_LANDYACHT_DIRECTION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Land yacht direction: {} degrees".format(
                monitor_message.direction))

        elif choice == 5:
            # Get the (absolute) position of the land yacht
            # Create and send a GET_LANDYACHT_POSITION message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.GET_LANDYACHT_POSITION)
            control_queue.put(control_message)
            # Wait for the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Land yacht position: {}, {}".format(
                monitor_message.position_x, monitor_message.position_y))

        elif choice == 6:
            # Turn the steering wheel by the angle specified by the user
            angle = input("Enter the new angle: ")
            # Create and send a TURN_STEERING_WHEEL message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.TURN_STEERING_WHEEL,
                angle=angle)
            control_queue.put(control_message)

        elif choice == 7:
            # Turn the sail by the angle specified by the user
            angle = input("Enter the new angle: ")
            # Create and send a TURN_SAIL message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.TURN_SAIL,
                angle=angle)
            control_queue.put(control_message)

        elif choice == 8:
            # Navigate to the direction specified by the user
            direction = input("Enter the new direction: ")
            # Create and send a NAVIGATE_TO_DIRECTION message to the AI
            command_message = CommandMessage(
                CommandMessageType.NAVIGATE_TO_DIRECTION,
                direction=direction)
            command_queue.put(command_message)

        elif choice == 9:
            # Navigate to the position specified by the user
            position_x = input("Enter the X position: ")
            position_y = input("Enter the Y position: ")
            # Create and send a NAVIGATE_TO_POSITION message to the AI
            command_message = CommandMessage(
                CommandMessageType.NAVIGATE_TO_POSITION,
                position_x=position_x,
                position_y=position_y)
            command_queue.put(command_message)

        elif choice == 10:
            # Stop the land yacht
            # Create and send a STOP_AI message to the AI
            command_message = CommandMessage(
                CommandMessageType.STOP_AI)
            command_queue.put(command_message)
            # Create and send a STOP_LANDYACHT message to the land yacht
            control_message = ControlMessage(
                ControlMessageType.STOP_LANDYACHT)
            control_queue.put(control_message)
            # Exit the loop and let the thread stop
            break

def display_help():
    """Displays the list of available operations"""
    print("Operations:")
    print(" 0 - Display help")
    print(" 1 - Get the angle of the steering wheel")
    print(" 2 - Get the angle of the sail")
    print(" 3 - Get the direction of the wind")
    print(" 4 - Get the direction of the land yacht")
    print(" 5 - Get the position of the land yacht")
    print(" 6 - Turn the steering wheel")
    print(" 7 - Turn the sail")
    print(" 8 - Navigate to direction")
    print(" 9 - Navigate to position")
    print("10 - Stop the land yacht")
