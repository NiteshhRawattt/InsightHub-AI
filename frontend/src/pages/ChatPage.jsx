import { useState } from "react";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import MessageInput from "../components/chat/MessageInput";

function ChatPage() {
  const [messages, setMessages] = useState([]);
  return (
    <div className="flex h-screen bg-surface-900">
      <Sidebar />

      <div className="flex flex-col flex-1">
        <ChatWindow messages={messages} />

        <MessageInput
          onSend={(text) => {

            const updatedMessages = [
              ...messages,
              {
                id: Date.now(),
                text,
                sender: "user",
              },
            ];

            setMessages(updatedMessages);

            console.log(updatedMessages);
          }}
        />
      </div>
    </div>
  );
}

export default ChatPage;