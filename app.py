from flask import Flask, render_template, Response, request
import cv2

#Initialize the Flask app
app = Flask(__name__)
action = None
img_bgs = []

def gen_frames():  
    camera = cv2.VideoCapture(0)
    dim = (1280,720)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if action == "Take":
                img_bgs.append(cv2.resize(frame, dim, interpolation=cv2.INTER_CUBIC))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET', 'POST'])
def index():
    global action
    action = None
    if request.method == "POST":
        if "take" in request.form:
            action = request.form.get("take")
        elif "track" in request.form:
            action = request.form.get("track")
        elif "stop" in request.form:
            action = request.form.get("stop")
    print(len(img_bgs))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)