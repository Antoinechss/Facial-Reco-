import cv2 as cv
from cam_access import CamFeedCV
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

feed = CamFeedCV(cv.VideoCapture(1)) # Set VideoCapture(0) as webcam default


# ----------------------
# Flask route for user interface
# ----------------------
@app.route('/')
def index():
    return render_template('control_panel.html')

# ----------------------
# Flask route for video feed
# ----------------------
@app.route('/video_feed')
def video_feed():
    return Response(feed.grab_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

# ----------------------
# Flask route for face coordinates
# ----------------------
@app.route("/face_frames")
def face_frames():
    return jsonify(feed.faces_coords) # list of x,y,w,h dicts

# ----------------------
# Flask route for face id on click
# ----------------------
@app.route('/face/<int:face_id>')
def face_detail(face_id):
    return f"<h1>You clicked on Face #{face_id + 1}</h1><p>This page was opened in a new tab!</p>"


#############################################################################
#############################################################################

if __name__ == '__main__':
    app.run(debug=True)



