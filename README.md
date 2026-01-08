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

### Use Case of EntryExitCount.AI  
EntryExitCount.AI is designed to automatically monitor and manage human movement in real time by accurately counting the number of people entering and exiting a defined area using surveillance cameras. The system is deployed at entry and exit points such as doors, corridors, gates, or checkpoints, where it continuously analyzes live video streams to detect and track individuals. By applying a line-crossing algorithm, the system determines the direction of movement and updates entry and exit counts without manual intervention. The live data is displayed on a web-based dashboard, allowing security personnel or administrators to monitor occupancy levels in real time. In addition, the system stores historical entry-exit data for further analysis and generates alerts when predefined crowd thresholds are exceeded. This use case is particularly effective in environments such as shopping malls, offices, educational institutions, hospitals, transportation hubs, and public venues, where accurate crowd monitoring, safety management, and data-driven decision-making are critical.  

### Advantages of EntryExitCount.AI

#### 1.Accurate Entry–Exit Counting  
Uses a line-crossing algorithm with object tracking to avoid double counting and false detections.  

#### 2.Real-Time Monitoring  
Provides live video feed and real-time IN/OUT counters through a web-based dashboard.  

#### 3.Automated & Contactless System  
Eliminates the need for manual counting, reducing human error and operational cost.  

#### 4.Scalable & Flexible  
Can be deployed across multiple locations such as malls, offices, or public spaces with minimal changes.  

#### 5.Data-Driven Insights  
Stores historical data and visualizes trends using charts for better decision-making.  

#### 6.Improved Safety & Crowd Control  
Generates alerts when crowd limits are exceeded, supporting proactive safety management.  

#### 7.Cost-Effective Solution  
Built using open-source technologies, making it affordable compared to traditional hardware-based systems.  
