import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# DeepSORT tracker
tracker = DeepSort(max_age=30)

# Virtual vertical line position
LINE_X = 320

# Global counters
count_in = 0
count_out = 0

# Track previous x-position of each person
track_previous_x = {}

# Track already counted IDs
counted_ids = set()


def process_frame(frame):
    global count_in, count_out

    detections = []

    # YOLO detection
    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        if int(box.cls[0]) == 0:  # person class
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            detections.append(
                ([x1, y1, x2 - x1, y2 - y1], conf, "person")
            )

    # DeepSORT tracking
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())

        # Center point
        cx = (l + r) // 2
        cy = (t + b) // 2

        # First time seeing this ID
        if track_id not in track_previous_x:
            track_previous_x[track_id] = cx
            continue

        prev_x = track_previous_x[track_id]

        # 🔥 LINE CROSSING LOGIC
        if track_id not in counted_ids:

            # LEFT → RIGHT  → IN
            if prev_x < LINE_X and cx >= LINE_X:
                count_in += 1
                counted_ids.add(track_id)

            # RIGHT → LEFT → OUT
            elif prev_x > LINE_X and cx <= LINE_X:
                count_out += 1
                counted_ids.add(track_id)

        # Update previous position
        track_previous_x[track_id] = cx

        # Draw bounding box and ID
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"ID {track_id}",
            (l, t - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

    # Draw counting line
    cv2.line(
        frame,
        (LINE_X, 0),
        (LINE_X, frame.shape[0]),
        (255, 0, 0),
        2
    )

    # Display counts on frame
    cv2.putText(
        frame,
        f"IN: {count_in}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    cv2.putText(
        frame,
        f"OUT: {count_out}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    return frame


def get_counts():
    return count_in, count_out
