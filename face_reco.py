import cv2 as cv
from cam_access import CamFeedCV
from flask import Flask, render_template, Response

app = Flask(__name__)

# Retrieving live video from webcam
# Completing face recognition and framing
# Sending stream onto web

feed = CamFeedCV(cv.VideoCapture(1)) # Set VideoCapture(0) as webcam default

@app.route('/')
def index():
    return render_template('control_panel.html')  # HTML with video tag

@app.route('/video_feed')
def video_feed():
    return Response(feed.grab_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)



