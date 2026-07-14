import { useState } from "react";
function MessageInput() {
    const [message, setMessage] = useState("");
    const handleSend = () => {

        if (message.trim() === "") return;

        alert(message);
        setMessage("");

    };
    return (
        <div className="border-t border-surface-500 p-5">

            <div className="flex gap-3">

                <input
                    type="text"
                    placeholder="Ask anything..."
                    className="input-field flex-1"

                    value={message}

                    onChange={(e) => setMessage(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            handleSend();
                        }
                    }}
                />

                <button
                    className="btn-primary"
                    onClick={handleSend}
                >
                    Send
                </button>

            </div>

        </div>
    );
}

export default MessageInput;