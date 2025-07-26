import ConversationSidebar from "./ConversationHistoryPanel";
import MessageList from "./MessageList";
import UserInput from "./UserInput";

export default function ChatWindow() {
  return (
    <div className="flex h-full">
      <ConversationSidebar />
      <div className="flex flex-col flex-1 p-4">
        <MessageList />
        <UserInput />
      </div>
    </div>
  );
}
