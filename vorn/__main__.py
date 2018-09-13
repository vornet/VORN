import megapi
import picamera
import vorn

megaPi = megapi.MegaPi()
piCamera = picamera.PiCamera()

vorn = vorn.Vorn(megaPi, piCamera)
vorn.start()