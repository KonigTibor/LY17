"""Contains message type enumerations and message classes"""

from enum import Enum

# Command messages are sent from the skipper to the AI via the command queue
# They are high-level instructions like "Navigate to position 10, 20"

class CommandMessageType(Enum):
    """Implements the CommandMessageType enumeration"""
    TEST_AI = 100
    NAVIGATE_TO_DIRECTION = 101
    NAVIGATE_TO_POSITION = 102
    STOP_AI = 199

class CommandMessage(object):
    """Implements the CommandMessage class"""

    def __init__(self, message_type, direction=None, position_x=None, position_y=None):
        """Instantiates a CommandMessage"""
        self.message_type = message_type
        self.direction = direction
        self.position_x = position_x
        self.position_y = position_y

# Control messages are sent from the skipper and the AI to the land yacht via the control queue
# They are low-level instrctions eg. "Turn the steering wheel by 30 degrees"

class ControlMessageType(Enum):
    """Implements the ControlMessageType enumeration"""
    TEST_LANDYACHT = 200
    GET_STEERING_WHEEL_ANGLE = 201
    GET_SAIL_ANGLE = 202
    GET_WIND_DIRECTION = 203
    GET_LANDYACHT_DIRECTION = 204
    GET_LANDYACHT_POSITION = 205
    TURN_STEERING_WHEEL = 206
    TURN_SAIL = 207
    STOP_LANDYACHT = 299

class ControlMessage(object):
    """Implements the ControlMessage class"""

    def __init__(self, message_type, angle=None):
        """Instantiates a ControlMessage"""
        self.message_type = message_type
        self.angle = angle

# Monitor messages are sent from the land yacht to the skipper and the AI via the monitor queue
# They contain monitoring information about the land yacht and the devices connected to it

class MonitorMessageType(Enum):
    """Implements the MonitorMessageType enumeration"""
    #TEST_SKIPPER = 300
    STEERING_WHEEL_ANGLE = 301
    SAIL_ANGLE = 302
    WIND_DIRECTION = 303
    LANDYACHT_DIRECTION = 304
    LANDYACHT_POSITION = 305

class MonitorMessage(object):
    """Implements the MonitorMessage class"""

    def __init__(self, message_type, angle=None, direction=None, position_x=None, position_y=None):
        """Instantiates a MonitorMessage"""
        self.message_type = message_type
        self.angle = angle
        self.direction = direction
        self.position_x = position_x
        self.position_y = position_y
