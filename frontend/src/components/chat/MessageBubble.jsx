import ReactMarkdown from "react-markdown";
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
               <ReactMarkdown
    className={
        isUser
            ? "max-w-none"
            : "prose prose-invert max-w-none prose-headings:text-white prose-p:text-white prose-strong:text-white prose-li:text-white prose-code:text-cyan-300"
    }
>
    {message.text}
</ReactMarkdown>
            </div>

        </div>

    );
}

export default MessageBubble;