from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def index(request):
    return render(request, "index.html")

def generate(request):
    prompt = request.GET.get("user_input")
    if not prompt:
        return JsonResponse({"error": "No prompt provided"})

    def generate_events():
        payload = {
            "model": "llama3.2", # Use `mistral` if you have a more powerful GPU.
            "system": "You are an academic assistant AI. You must strictly answer only educational queries. If the user asks about anything non-educational (such as personal advice, explicit content, opinions, or unrelated topics), you must firmly reject the request and remind them to ask academic questions only. Do not engage in casual, personal, or inappropriate discussions.",
            "prompt": prompt,
            "stream": True,
            "stop": ["Sorry, I can't answer that.", "I am only programmed for academic queries."]
        }
        
        try:
            with requests.post(OLLAMA_API_URL, json=payload, stream=True) as ollama_stream:
                for line in ollama_stream.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        yield f"data: {json.dumps({'chunk': chunk.get('response', '')})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        finally:
            yield "event: close\ndata: {}\n\n"

    return StreamingHttpResponse(generate_events(), content_type="text/event-stream")
