# AI-Assisted Study Tool

This is a Flask-based web application that provides an AI-powered academic assistant. The assistant helps with various academic topics, including math, science, history, literature, and coding. The application uses the **Mistral** language model and integrates with an AI backend via the **Ollama API**.

## Features
- **AI-powered chatbot** for academic support
- **Supports coding-related queries**
- **Real-time responses using server-sent events (SSE)**
- **Bootstrap dark mode theme** for modern UI design
- **User-friendly interface** with a navbar, input field, and chat display
- **Strict filtering of non-academic prompts**

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **AI Model:** Mistral (via Ollama API)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (3.8+ recommended)
- Flask
- `requests` library for API calls
- Ollama (running locally on `localhost:11434`)

### Steps to Run Locally
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Install dependencies:**
   ```sh
   pip install flask requests
   ```
3. **Download Ollama and the Mistral LLM model:**
     - Download Ollama from [their official site](https://ollama.com/). Then type the following commands in the windows terminal one-by-one:

   ```sh
   ollama run mistral
   ```

   ```sh
   ollama serve
   ```

4. **Run the Flask application:**
   ```sh
   python app.py
   ```
5. **Access the website** by opening `http://127.0.0.1:5000/` in your browser.

## File Structure
```
├── static/
│   ├── styles.css  # Custom styles
│   ├── scripts.js  # Client-side logic
├── templates/
│   ├── index.html  # Main UI layout
├── app.py          # Flask backend logic
├── README.md       # Project documentation
```

## API Usage
The app communicates with **Ollama API** to generate responses. The main API endpoint used:
```plaintext
http://localhost:11434/api/generate
```

## Academic Prompt Filtering
The chatbot strictly answers academic-related queries. If a user enters a non-academic prompt, they receive an error message.

## Contributing
Feel free to contribute by submitting pull requests! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## Future Plans
At it's current state, this project is far from a finished project. There are many plans for it's future, including but not limited to:
1. Adding more resources
    - There is a navbar tab dedicated to resources which is currently empty. In the future, we have plans to implement more resources related to academics such as popular books, lectures, and previous year papers. 
2. Integrating a signup/login page (Back-end)
    - Currently, the website has no proper back-end. In the future, we plan to integrate a login page, such that the user will be able to visit and continue their previous chats with the AI assistant.
3. Integrating a social-media like environment
    - We have plans to integrate a forum-site like environment in which students would be able to post their queries in an open-space, and other students will be able to answer those queries. 
    - We also have plans for a game-like system in this environment, which will encourage the users to interact more frequently with other students.

**Developed by [Team_Name] of Christ College of Engineering, Irinjalakuda.**