# AI-Assisted Study Tool

This is a Django-based web application designed to serve as an AI-powered academic assistant. The platform aims to provide students with an interactive learning environment that integrates AI-driven tutoring, a collaborative student community, and gamification features to encourage participation. The assistant is powered by **Mistral/Llama3.2** through the **Ollama API**, ensuring real-time, academic-focused responses.

## Features
- **AI-powered chatbot** for academic support across various subjects
- **User authentication system** for personalized experiences and saved progress
- **Student community forum** for discussions, Q&A, and resource sharing
- **Real-time responses using server-sent events (SSE)**
- **Gamification features** to incentivize participation (planned)
- **Modern UI with React integration** (planned)
- **Strict academic filtering** to ensure relevance

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap), JavaScript (Planned React Integration)
- **Database:** PostgreSQL / SQLite (for user authentication & chat history)
- **AI Model:** Mistral/Llama3.2 (via Ollama API)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (3.8+ recommended)
- Django
- `requests` library for API calls
- PostgreSQL (optional; can use SQLite for development)
- Ollama (running locally on `localhost:11434`)

### Steps to Run Locally
1. **Clone the repository:**
   ```sh
   git clone https://github.com/WanderingHumanid/ai-study-assistant.git
   cd ai-study-assistant
   ```
2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**

4. **Download and set up Ollama:**
   - Install Ollama from [their official site](https://ollama.com/).
   - Download the required AI model:
     ```sh
     ollama run llama3.2  # or `ollama run mistral` if you have a more powerful GPU
     ```
   - Serve the model in a separate terminal:
     ```sh
     ollama serve
     ```
5. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```
6. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```
7. **Run the Django server:**
   ```sh
   python manage.py runserver
   ```
8. **Access the website** by opening `http://127.0.0.1:8000/` in your browser.

## File Structure
```
├── static/
│   ├── styles.css  # Custom styles
│   ├── scripts.js  # Client-side logic
├── templates/
│   ├── index.html  # Main UI layout
├── ai_study_tool/
│   ├── settings.py # Django project settings
│   ├── urls.py     # URL routing
│   ├── views.py    # Backend logic
│   ├── models.py   # Database models
├── manage.py       # Django CLI script
├── README.md       # Project documentation
```

## API Usage
The app communicates with **Ollama API** to generate responses. The primary API endpoint used:
```plaintext
http://localhost:11434/api/generate
```

## Academic Prompt Filtering
The chatbot strictly answers academic-related queries. If a user enters a non-academic prompt, they receive an error message.

## Future Plans
This project is still in the early stages of development. Planned features include:
1. **Expanding available resources**
   - A dedicated resources tab will include books, lectures, and past papers (if targeting a specific academic field).
2. **Full backend integration with user authentication**
   - Users will be able to log in, save chat histories, and track their progress.
3. **Student community feature**
   - A forum-like environment where students can ask and answer questions.
   - AI-powered content analysis for discussions.
4. **Gamification system**
   - Streaks, virtual rewards, and leaderboards to encourage participation.
5. **React-based modern UI**
   - Improved responsiveness and user experience.

## Contributing
To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

**Developed by Team Techverse of S2 CSE-C from Christ College of Engineering, Irinjalakuda.**