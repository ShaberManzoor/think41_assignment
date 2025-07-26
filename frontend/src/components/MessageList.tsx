
import { useChatStore } from "../store/useChatStore";
import Message from "./Message";

export default function MessageList() {
  const messages = useChatStore((s) => s.messages);
  return (
    <div className="flex-1 overflow-y-auto space-y-2 mb-4">
      {messages.map((msg, idx) => (
        <Message key={idx} role={msg.role} content={msg.content} />
      ))}
    </div>
  );
}
