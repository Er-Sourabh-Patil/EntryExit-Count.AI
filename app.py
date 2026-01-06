from flask import Flask, render_template, Response, jsonify
import cv2
from datetime import date
from database import db, CountData, AlertLog
from detection import process_frame, get_counts
from alerts import check_alert

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///people.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

cap = cv2.VideoCapture(0)
last_saved_date = None


def save_daily_data(cin, cout):
    global last_saved_date
    today = date.today()

    with app.app_context():
        if last_saved_date != today:
            db.session.add(
                CountData(
                    in_count=cin,
                    out_count=cout,
                    date=today
                )
            )
            db.session.commit()
            last_saved_date = today


def log_alert(message):
    with app.app_context():
        db.session.add(AlertLog(message=message))
        db.session.commit()


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.resize(frame, (640, 480))
        frame = process_frame(frame)

        cin, cout = get_counts()
        current_people = cin - cout

        # 🔒 SAFE background operations
        save_daily_data(cin, cout)

        alert, msg = check_alert(current_people)
        if alert:
            log_alert(msg)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/video")
def video():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/live-counts")
def live_counts():
    cin, cout = get_counts()
    return jsonify({"in": cin, "out": cout})


@app.route("/history")
def history():
    data = CountData.query.order_by(CountData.date.desc()).all()
    return render_template("history.html", data=data)


@app.route("/alerts")
def alerts():
    logs = AlertLog.query.order_by(AlertLog.timestamp.desc()).all()
    return render_template("alerts.html", logs=logs)


@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/chart-data")
def chart_data():
    records = CountData.query.order_by(CountData.date).all()
    return jsonify({
        "dates": [r.date.strftime("%d-%m-%Y") for r in records],
        "in_counts": [r.in_count for r in records],
        "out_counts": [r.out_count for r in records]
    })


if __name__ == "__main__":
    app.run(debug=True)
