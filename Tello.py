from djitellopy import Tello
from gamepad import XboxController
import keyboard
import cv2


if __name__ == "__main__":
    tello = Tello()

    tello.connect()

    tello.takeoff()

    controller = XboxController()

    tello.streamon()

    while True:
        if keyboard.is_pressed("Esc"):
            break

        tello.send_rc_control(round(controller.read()[0] * 100), round(controller.read()[1] * 100), round(controller.read()[3] * 100), round(controller.read()[2] * 100))


        img = tello.get_frame_read().frame
        img = cv2.resize(img, (1080, 720))

        cv2.imshow("DroneCapture", img)
        cv2.waitKey(1)

    tello.land()
