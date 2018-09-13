
class EncoderMotor:
    
    def __init__(self, megapi, slot):
        self._megapi = megapi
        self._slot = slot

    def run(self, power):
        self._megapi.encoderMotorRun(self._slot, power)
        