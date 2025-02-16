from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    prompt = request.args.get('user_input')
    if not prompt:
        return Response("data: {'error': 'No prompt provided'}\n\n", mimetype='text/event-stream')

    def generate_events():
        payload = {
            "model": "mistral",
            "system": "You are an academic assistant. Only answer questions related to academics educational subjects. If a question is off-topic, politely refuse to answer and guide them on what type of questions they're supposed to ask.",
            "prompt": prompt,
            "stream": True
        }
        
        try:
            with requests.post(OLLAMA_API_URL, json=payload, stream=True) as ollama_stream:
                for line in ollama_stream.iter_lines():
                    if line:
                        chunk = json.loads(line.decode('utf-8'))
                        yield f"data: {json.dumps({'chunk': chunk.get('response', '')})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        finally:
            yield "event: close\ndata: {}\n\n"
    
    return Response(generate_events(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)