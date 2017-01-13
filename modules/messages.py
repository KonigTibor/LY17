"""Contains message type enumerations and message classes"""

from enum import Enum, auto

# Command messages are sent from the skipper to the AI via the command queue
# They are high-level instructions like "Navigate to position 10, 20"

class CommandMessageType(Enum):
    """Implements the CommandMessageType enumeration"""
    TEST_AI = 100
    NAVIGATE_TO_DIRECTION = auto()
    NAVIGATE_TO_POSITION = auto()
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
    GET_STEERING_WHEEL_ANGLE = auto()
    GET_SAIL_ANGLE = auto()
    GET_WIND_DIRECTION = auto()
    GET_LANDYACHT_DIRECTION = auto()
    GET_LANDYACHT_POSITION = auto()
    GET_LANDYACHT_SPEED = auto()
    TURN_STEERING_WHEEL = auto()
    TURN_SAIL = auto()
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
    TEST_SKIPPER = 300
    STEERING_WHEEL_ANGLE = auto()
    SAIL_ANGLE = auto()
    WIND_DIRECTION = auto()
    LANDYACHT_DIRECTION = auto()
    LANDYACHT_POSITION = auto()
    LANDYACHT_SPEED = auto()

class MonitorMessage(object):
    """Implements the MonitorMessage class"""

    def __init__(self, message_type, angle=None, direction=None, position_x=None, position_y=None, speed=None):
        """Instantiates a MonitorMessage"""
        self.message_type = message_type
        self.angle = angle
        self.direction = direction
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
