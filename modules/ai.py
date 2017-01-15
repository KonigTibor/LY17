"""Contains the ai module"""

from queue import Queue, Empty

from .messages import CommandMessageType, CommandMessage
from .messages import ControlMessageType, ControlMessage
from .messages import MonitorMessageType

def ai(command_queue, control_queue, monitor_queue):
    """Implements the ai module"""

    # Variable to store the last message
    command_message = CommandMessage(CommandMessageType.CONTINUE_COURSE)

    # Run until a STOP_AI command message is received
    while True:

        # Try to get the next message from the command queue
        try:

            # If there is a new message then get it and store it
            command_message = command_queue.get(block=False)

        # When there is no new message process the last one
        except Empty:

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
