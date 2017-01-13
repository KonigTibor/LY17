"""Contains generic device classes"""

SERVO_CENTER = 0
SERVO_MIN_ANGLE = -90
SERVO_MAX_ANGLE = 90

class Controller(object):
    """Implements the Controller class"""

    def __init__(self, controller_type=None, hardware=None):
        self.controller_type = controller_type
        self.hardware = hardware

class Servo(object):
    """Implements the Servo class"""

    def __init__(self, controller, pin=None, angle=SERVO_CENTER, min_angle=SERVO_MIN_ANGLE, max_angle=SERVO_MAX_ANGLE):
        """Instantiates a Servo"""
        self.controller = controller
        self.pin = pin
        self.angle = angle
        self.min_angle = min_angle
        self.max_angle = max_angle

    def get_angle(self):
        """Returns the current angle of the servo"""
        return self.angle

    def turn(self, angle):
        """Turns the servo by the angle specified"""

        # Make sure the angle is between the minimum and maximum angles
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle

        # Set the current angle
        self.angle = angle

class RotationSensor(object):
    """Implements the RotationSensor class"""

    def __init__(self, controller, pin=None):
        """Instantiates a RotationSensor"""
        controller = controller
        pin = pin

    def get_direction(self):
        """Returns the current direction of the sensor"""
        # HACK: return a constant
        self.direction = 0
        return self.direction

class Compass(object):
    """Implements the Compass class"""

    def __init__(self, controller, pin=None):
        """Instantiates a Compass"""
        controller = controller
        pin = pin

    def get_direction(self):
        """Returns the current direction of the compass"""
        # HACK: return a constant
        self.direction = 0
        return self.direction

class GPS(object):
    """Implements the GPS class"""

    def __init__(self, controller, pin=None):
        """Instantiates a GPS"""
        controller = controller
        pin = pin

    def get_position_x(self):
        """Returns the X coordinate of the current position"""
        # HACK: return a constant
        self.position_x = 0
        return self.position_x

    def get_position_y(self):
        """Returns the Y coordinate of the current position"""
        # HACK: return a constant
        self.position_y = 0
        return self.position_y

class Speedometer(object):
    """Implements the Speedometer class"""

    def __init__(self, controller, pin=None):
        """Instantiates a Speedometer"""
        self.controller = controller
        self.pin = pin

    def get_speed(self):
        # HACK: return a constant
        self.speed = 0
        return self.speed
