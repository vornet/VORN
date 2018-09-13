import locomotion
import motors
import sensors
import time

class Vorn:    
    def __init__(self, megapi, piCamera):
        self._megapi = megapi
        self._piCamera = piCamera
        leftMotor = motors.EncoderMotor(megapi, 1)
        rightMotor = motors.EncoderMotor(megapi, 2)
        self._locomotion = locomotion.Locomotion(leftMotor, rightMotor)
        self._forwardUltrasonic = sensors.UltrasonicSensor(megapi, 8)        
        self._camera = sensors.CameraSensor(piCamera)

    def start(self):
        self._megapi.start()
        self._piCamera.start_preview()
        # self._camera..stop_preview()
        #self._locomotion.moveForward(500)
        
        time.sleep(0.1)

        while(1):
            try:                
                self._forwardUltrasonic.read()
                print("current ultrasonic reading: {}".format(self._forwardUltrasonic.get_value()))

                if self._forwardUltrasonic.get_value() == 400:
                    continue

                if self._forwardUltrasonic.get_value() < 15:
                    self._locomotion.move_backward(75)
                    time.sleep(5)
                    self._locomotion.turn_left(100)
                    time.sleep(5)
                    self._locomotion.turn_right(100)
                    time.sleep(5)
                    self._locomotion.stop()
                    self._camera.capture_image()
                    break
                else:
                    self._locomotion.move_forward(75)
                
            except Exception as e:
                print(e)
            time.sleep(0.1)
        
