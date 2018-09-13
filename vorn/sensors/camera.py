
class CameraSensor:
    def __init__(self, camera):
        self._camera = camera
        self._last_image = None
        self._index = 0

    def capture_image(self):
        self._index += 1
        self._camera.capture('/home/pi/current_image_{}.jpg'.format(self._index))
