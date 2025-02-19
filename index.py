from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import cross_origin
from router.quanli1.hoso import hosos
from router.quanli1.home import homes
from router.quanli1.maneger import manegers
from router.quanli1.phongbenh import phongbenhs
from router.quanli1.benhnhan import benhnhans
from database import SessionLocal
from models import HealthData
import logging



app = Flask(__name__, template_folder="views", static_folder="assets")
app.config["SECRET_KEY"] = "test123"
app.config["DEBUG"] = True
socket = SocketIO(app, cors_allowed_origins="*")

log = logging.getLogger("werkzeug")
log.disabled = True

app.register_blueprint(homes)
app.register_blueprint(hosos)
app.register_blueprint(phongbenhs)
app.register_blueprint(benhnhans)
app.register_blueprint(manegers)

def add_health_data(heart_rate: float, spo2: float, user_id: int):
    """Thêm dữ liệu sức khỏe vào database."""
    try:
        with SessionLocal() as db:
            new_record = HealthData(heartRate=heart_rate, spo2=spo2, user_id=1)
            db.add(new_record)
            db.commit()
            db.refresh(new_record)
            print(f"Inserted Health Data ID: {new_record.id}")
    except Exception as e:
        print(f"Error inserting health data: {e}")

@cross_origin()
@socket.on("data")
def handle_data(data):
    print(f"Received data: {data}")
    try:
        heart_rate = float(data.get("heart_rate"))
        spo2 = float(data.get("spo2"))
        user_id = int(data.get("user_id"))
        add_health_data(heart_rate, spo2, user_id)
        socket.emit("clientData", {"status": "success", "message": "Data saved"})
    except Exception as e:
        print(f"Error processing data: {e}")
        socket.emit("clientData", {"status": "error", "message": str(e)})

@cross_origin()
@socket.on("connect")
def on_connect():
    print("Client connected")
    socket.emit("clientData", "hi")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=False)
