
import { useEffect, useState } from "react";
import { useChatStore } from "../store/useChatStore";

export default function ConversationSidebar() {
  const { setMessages, setSessionId } = useChatStore();
  const [sessions, setSessions] = useState<string[]>([]);

  const fetchSessions = async () => {
    const res = await fetch("http://localhost:8000/api/conversations");
    const data = await res.json();
    setSessions(data);
  };

  const loadSession = async (id: string) => {
    const res = await fetch(`http://localhost:8000/api/history/${id}`);
    const data = await res.json();
    setSessionId(id);
    setMessages(data);
  };

  useEffect(() => {
    fetchSessions();
  }, []);

  return (
    <div className="w-60 bg-white border-r p-4 overflow-y-auto">
      <h2 className="font-semibold mb-2">Conversations</h2>
      {sessions.map((id) => (
        <div
          key={id}
          className="text-sm text-blue-600 cursor-pointer hover:underline mb-1"
          onClick={() => loadSession(id)}
        >
          {id.slice(0, 8)}
        </div>
      ))}
    </div>
  );
}
