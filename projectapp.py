from flask import Flask, render_template, request, Response
import cv2

app = Flask(__name__)
capture = cv2.VideoCapture(-1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def gen_frames():  
    while True:
        ref, frame = capture.read()  # 현재 영상을 받아옴
        if not ref:
            break
        else:
            ref, buffer = cv2.imencode('.jpg', frame)   # 현재 영상을 그림파일형태로 바꿈
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # 그림파일들을 쌓아두고 호출을 기다림

@app.route('/')
def index():
        return render_template('project.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame') # 그림파일들을 쌓아서 보여줌


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
