
import cv2 as cv

# loading the face recognition haar cascade classifier
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

class CamFeedCV:
    def __init__(self, cam_directory):
        self.cam = cam_directory
        self.faces_coords = []

    def grab_frame(self):
        while True:
            # reading camera feed frame by frame
            ret, frame = self.cam.read()
            # checking if camera is on
            if not ret :
                break

            # ----------------------
            # Running face recognition and framing
            # ----------------------

            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame_gray = cv.equalizeHist(frame_gray)

            faces_coordinates = face_cascade.detectMultiScale(frame_gray)

            self.faces_coords = [{"x":int(x), "y":int(y), "w":int(w), "h":int(h)} for x,y,w,h in faces_coordinates]

            for x,y,w,h in faces_coordinates:
                frame = cv.rectangle(frame, (x,y),(x+w,y+h), (255,0,255), 4)

            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


    def __del__(self):
        if self.cam.isOpened():
            self.cam.release()

