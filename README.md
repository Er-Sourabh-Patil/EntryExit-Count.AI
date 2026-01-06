# EntryExit-Count.AI
EntryExitCount.AI is an AI-powered real-time people entry–exit counting system designed to accurately monitor human movement across defined areas using computer vision. The system leverages YOLOv8 for person detection, DeepSORT for multi-object tracking, and a line-crossing algorithm to reliably count people entering and exiting a space. It features a live web dashboard with real-time counters, historical data storage, visual analytics, and crowd safety alerts.
The solution is highly suitable for crowd monitoring, occupancy analysis, and safety management in environments such as shopping malls, offices, educational institutions, hospitals, airports, railway stations, public buildings, event venues, and smart city surveillance systems. By providing actionable insights through live and historical data, EntryExitCount.AI helps organizations improve space utilization, crowd control, operational efficiency, and public safety.

## Project Structure 
EntryExitCount.AI/  
│  
├── app.py  
├── detection.py  
├── alerts.py  
├── database.py  
├── people.db  
│  
├── templates/  
│   ├── base.html  
│   ├── dashboard.html  
│   ├── history.html  
│   ├── alerts.html  
│   └── charts.html  
│  
├── static/  
│   ├── css/  
│   │   └── style.css  
│   ├── images/  
│   │   └── entryexitcount_ai_banner.png  
│   └── alert.mp3  
│  
├── yolov8n.pt  
├── venv/  
└── README.md  



## Steps to run 
1. Create and activate virtual environmnent
   ```
   python -m venv venv
   venv\Scripts\activate.ps1

2. Install Required Libraries
   ```
   pip install ultralytics opencv-python deep-sort-realtime flask flask-sqlalchemy

3. Run the Application
   ```
   python app.py

4. Open in Browser
   ```
   http://127.0.0.1:5000



