document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('save-message');
    const messageInput = document.getElementById('message-input');
    const messagesList = document.getElementById('messages-list');

    function loadMessages() {
        fetch('/load_messages')
            .then(response => response.json())
            .then(messages => {
                messagesList.innerHTML = '';
                messages.forEach(message => {
                    const messageElement = document.createElement('p');
                    messageElement.textContent = message;
                    messagesList.appendChild(messageElement);
                });
            })
            .catch(error => console.error('Erro ao carregar mensagens:', error));
    }

    function saveMessage() {
        const message = messageInput.value.trim();
        if (message === '') return;

        fetch('/save_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                messageInput.value = '';
                loadMessages();
            } else {
                console.error('Erro ao salvar a mensagem:', result.error);
            }
        })
        .catch(error => console.error('Erro na requisição:', error));
    }

    saveButton.addEventListener('click', saveMessage);
    loadMessages();
});
