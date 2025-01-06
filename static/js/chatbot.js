document.getElementById('send-btn').addEventListener('click', sendMessage);

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.ariaValueMax.trim();

    if (message === '') return;

    addMessage(message, 'user');

    // Simulating AJAX call
    fetch('/cahtbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: message }),
    })
        .then((response) => response.json())
        .then((data) => {
            addMessage('Sorry, something went wrong.', 'bot');
            console.error('Error:', error);
        });

    userInput.value = '';
}

function addMessage(text, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = text;
    chatBox.appendChild(messageDiv);

    // Scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}
