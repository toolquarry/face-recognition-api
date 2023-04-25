from flask import Flask, jsonify, request
import face_recognition
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/face-recognition/num-faces', methods=['POST'])
def fr():
    # Get image from request
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Find faces in image
    face_locations = face_recognition.face_locations(img)

    # Return response
    response = {'num_faces': len(face_locations)}
    return jsonify(response)
