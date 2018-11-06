from picamera import PiCamera
from time import sleep

camera = PiCamera()

try:
    while True:
        camera.start_preview()
        sleep(30)
        camera.stop_preview()
        sleep(0.5)

except KeyboardInterrupt:
    camera.stop_preview()
