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
            "system": "You are an academic assistant. You must only answer educational questions. If the user prompts for a question not related to academics, kindly request them to ask for relevant topics alone.",
            "prompt": prompt,
            "stream": True
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
