
class UltrasonicSensor:
    
    def __init__(self, megapi, slot):
        self._megapi = megapi
        self._slot = slot
        self._last_val = 400

    def read(self):
        self._megapi.ultrasonicSensorRead(self._slot, self._on_forward_ultrasonic_read)

    def get_value(self):
        return self._last_val

    def _on_forward_ultrasonic_read(self, val):
        self._last_val = val
    

