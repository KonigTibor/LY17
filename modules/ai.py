"""Contains the ai module"""

from .messages import CommandMessageType
from .messages import ControlMessageType, ControlMessage
from .messages import MonitorMessageType

def ai(command_queue, control_queue, monitor_queue):
    """Implements the ai module"""

    # Wait for messages from the command queue
    while True:

        # Get the next message from the command queue
        command_message = command_queue.get()

        # Process the message
        if command_message.message_type == CommandMessageType.TEST_AI:
            # Test the AI
            # TODO: implement self-testing
            pass

        elif command_message.message_type == CommandMessageType.NAVIGATE_TO_DIRECTION:
            # Navigate to the direction specified
            direction = command_message.direction
            # TODO: implement navigation

        elif command_message.message_type == CommandMessageType.NAVIGATE_TO_POSITION:
            # Navigate to the position specified
            position_x = command_message.position_x
            position_y = command_message.position_y
            # TODO: implement navigation

        elif command_message.message_type == CommandMessageType.STOP_AI:
            # Exit the loop and let the thread stop
            break
