document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.getElementById("chat-box");
    const typingIndicator = document.getElementById("typing-indicator");
    let currentBotMessage = null;

    document.getElementById("chat-form").addEventListener("submit", function(e) {
        e.preventDefault();
        const userInput = document.getElementById("user-input").value;
        if (!userInput.trim()) return;

        chatBox.innerHTML += `<div class='message-bubble user-message'><strong>You:</strong><br>${userInput}</div>`;
        currentBotMessage = document.createElement("div");
        currentBotMessage.className = "message-bubble bot-message";
        currentBotMessage.innerHTML = "<strong>Mistral:</strong><br><div class='bot-response-content'></div>";
        chatBox.appendChild(currentBotMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
        typingIndicator.style.display = "block";
        document.getElementById("user-input").disabled = true;
        
        const eventSource = new EventSource(`/generate?user_input=${encodeURIComponent(userInput)}`);
        let buffer = "";

        eventSource.onmessage = (e) => {
            const data = JSON.parse(e.data);
            if (data.error) {
                buffer += `<div class='text-danger'>${data.error}</div>`;
                currentBotMessage.querySelector(".bot-response-content").innerHTML = buffer;
                return;
            }
            buffer += data.chunk;
            currentBotMessage.querySelector(".bot-response-content").innerHTML = marked.parse(buffer);
            chatBox.scrollTop = chatBox.scrollHeight;
        };

        eventSource.onerror = () => {
            typingIndicator.style.display = "none";
            document.getElementById("user-input").disabled = false;
            eventSource.close();
        };

        document.getElementById("user-input").value = "";
    });
});