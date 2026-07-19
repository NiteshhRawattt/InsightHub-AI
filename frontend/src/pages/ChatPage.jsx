import { useState } from "react";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import MessageInput from "../components/chat/MessageInput";

function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  const [selectedDocument, setSelectedDocument] = useState(null);

  return (
    <div className="flex h-screen bg-surface-900">
      <Sidebar
        selectedDocument={selectedDocument}
        setSelectedDocument={setSelectedDocument}
      />

      <div className="flex flex-col flex-1">
        <ChatWindow
          messages={messages}
          isTyping={isTyping}
        />

        <MessageInput
          onSend={async (text) => {
            // User message add karo
            const userMessage = {
              id: Date.now(),
              text,
              sender: "user",
            };

            setMessages((prev) => [...prev, userMessage]);
            setIsTyping(true);

            // Empty assistant message
            const assistantId = Date.now() + 1;

            setMessages((prev) => [
              ...prev,
              {
                id: assistantId,
                text: "",
                sender: "assistant",
              },
            ]);

            try {
              const response = await fetch(
                "http://127.0.0.1:8000/api/v1/chat/",
                {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify({
                    message: text,
                    selected_document: selectedDocument,
                  }),
                }
              );

              const data = await response.json();

const fullText = data.reply;

let aiText = "";

for (const char of fullText) {
  console.log(char);
  aiText += char;

  setMessages((prev) =>
    prev.map((msg) =>
      msg.id === assistantId
        ? {
            ...msg,
            text: aiText,
          }
        : msg
    )
  );

  await new Promise((resolve) => setTimeout(resolve, 12));
}
            } catch (error) {
              console.error(error);
            } finally {
              setIsTyping(false);
            }
          }}
        />
      </div>
    </div>
  );
}

export default ChatPage;