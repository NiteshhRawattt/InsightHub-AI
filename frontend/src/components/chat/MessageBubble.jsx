function MessageBubble({ message }) {

    const isUser = message.sender === "user";

    return (

        <div
            className={`flex ${isUser ? "justify-end" : "justify-start"}`}
        >

            <div
                className={
                    isUser
                        ? "chat-bubble-user"
                        : "chat-bubble-assistant"
                }
            >
                {message.text}
            </div>

        </div>

    );
}

export default MessageBubble;