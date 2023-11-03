const modeBtn = document.getElementById("mode-btn");


modeBtn.addEventListener("click", function () {
    if (document.querySelector(".chat-container").style.background == "rgb(227, 227, 215)") {
        document.querySelector(".chat-container").style.background = "rgb(59, 50, 50)";
        document.querySelector("body").style.background = "rgb(59, 50, 50)";
    }
    else {
        document.querySelector(".chat-container").style.background = "rgb(227, 227, 215)";
        document.querySelector("body").style.background = "rgb(227, 227, 215)";

    }
})


// document.addEventListener('DOMContentLoaded', function () {
//     const chatBox = document.getElementById('chat-box');
//     const userInput = document.getElementById('user-input');
//     const sendButton = document.getElementById('send-button');

//     sendButton.addEventListener('click', function () {
//         const message = userInput.value.trim();
//         if (message !== '') {
//             appendUserMessage(message);
//             userInput.value = '';
//             // Add your chatbot logic here to generate a response.
//             const botResponse = "Chatbot : Sample bot response";
//             appendBotMessage(botResponse);
//         }
//     });

//     userInput.addEventListener('keyup', function (event) {
//         if (event.key === 'Enter') {
//             sendButton.click();
//         }
//     });

//     function appendBotMessage(message) {
//         const messageDiv = document.createElement('div');
//         messageDiv.classList.add('chat-message', 'bot');
//         messageDiv.textContent = message;
//         chatBox.appendChild(messageDiv);
//         chatBox.scrollTop = chatBox.scrollHeight;
//     }

//     function appendUserMessage(message) {
//         const messageDiv = document.createElement('div');
//         messageDiv.classList.add('chat-message', 'user');
//         messageDiv.textContent = message;
//         chatBox.appendChild(messageDiv);
//         chatBox.scrollTop = chatBox.scrollHeight;
//     }
// });


