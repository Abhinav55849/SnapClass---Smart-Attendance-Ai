# SnapClass - Smart Attendance AI

AI-powered attendance system built with Streamlit and Supabase. Teachers can take attendance using face recognition or voice, and students can enroll and view their records.

## Features

- Create and share subjects
- Student enrollment
- Face-recognition attendance from class photos
- Voice-based attendance
- Teacher and student dashboards

## Tech Stack

- Streamlit (UI)
- Supabase (database)
- Python face and voice pipelines

## Setup

1. Clone the repo and create a virtual environment:
```
   git clone https://github.com/Abhinav55849/SnapClass---Smart-Attendance-Ai.git
   cd SnapClass---Smart-Attendance-Ai
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```

2. Create `.streamlit/secrets.toml`:
```toml
   SUPABASE_URL = "your-supabase-url"
   SUPABASE_KEY = "your-supabase-key"
```

3. Run the app:
```
   streamlit run app.py
```

## Project Structure

- `app.py` - entry point
- `src/screens` - home, teacher and student screens
- `src/components` - dialogs and UI components
- `src/pipelines` - face and voice processing
- `src/database` - Supabase connection and queries