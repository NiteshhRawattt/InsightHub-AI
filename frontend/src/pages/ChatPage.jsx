import { useState } from "react";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import MessageInput from "../components/chat/MessageInput";

function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  return (
    <div className="flex h-screen bg-surface-900">
      <Sidebar />

      <div className="flex flex-col flex-1">
        <ChatWindow
        messages={messages}
        isTyping={isTyping}
        />

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
            setIsTyping(true);
            setTimeout(() => {

               setMessages((prev) => [

                  ...prev,

                {
                  id: Date.now() + 1,
                  text: "This is a fake AI response.",
                  sender: "assistant",
                },

            ]);
            setIsTyping(false);

          }, 1000);


            console.log(updatedMessages);
          }}
        />
      </div>
    </div>
  );
}

export default ChatPage;