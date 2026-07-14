import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import MessageInput from "../components/chat/MessageInput";

function ChatPage() {
  return (
    <div className="flex h-screen bg-surface-900">
      <Sidebar />

      <div className="flex flex-col flex-1">
        <ChatWindow />

        <MessageInput />
      </div>
    </div>
  );
}

export default ChatPage;