import { useState } from "react";
import { useChatStore } from "../store/useChatStore";

export default function UserInput() {
  const [input, setInput] = useState("");
  const { sessionId, addMessage, setLoading, setMessages, setSessionId } =
    useChatStore();

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: "user", content: input } as const;
    addMessage(userMsg);
    setInput("");
    setLoading(true);

    const res = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input, conversation_id: sessionId }),
    });

    const data = await res.json();
    if (data.conversation_id) setSessionId(data.conversation_id);
    setMessages(data.history);
    setLoading(false);
  };

  return (
    <div className="flex items-center space-x-2">
      <input
        className="flex-1 p-2 border rounded"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
      />
      <button
        onClick={sendMessage}
        className="px-4 py-2 bg-blue-500 text-white rounded"
      >
        Send
      </button>
    </div>
  );
}
