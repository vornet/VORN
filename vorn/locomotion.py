
class Locomotion:

    def __init__(self, leftMotor, rightMotor):
        self._leftMotor = leftMotor
        self._rightMotor = rightMotor

    def stop(self):
        self._leftMotor.run(0)
        self._rightMotor.run(0)

    def move_forward(self, speed):
        self._leftMotor.run(speed)
        self._rightMotor.run(-speed)

    def move_backward(self, speed):
        self._leftMotor.run(-speed)
        self._rightMotor.run(speed)

    def turn_left(self, speed):
        self._leftMotor.run(speed)
        self._rightMotor.run(speed)

    def turn_right(self, speed):
        self._leftMotor.run(-speed)
        self._rightMotor.run(-speed)
