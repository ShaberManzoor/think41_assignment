import React, { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';

type MessageType = {
  sender: 'user' | 'ai';
  text: string;
};

const ChatWindow: React.FC = () => {
  const [messages, setMessages] = useState<MessageType[]>([]);

  const sendMessage = async (text: string) => {
    const userMessage: MessageType = { sender: 'user', text };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });

      const data = await res.json();
      const aiMessage: MessageType = { sender: 'ai', text: data.response };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="flex flex-col max-w-2xl mx-auto h-screen p-4 bg-white border rounded shadow">
      <h2 className="text-2xl font-bold mb-4 text-center">
        🧠 AI Chat Assistant
      </h2>
      <MessageList messages={messages} />
      <UserInput onSend={sendMessage} />
    </div>
  );
};

export default ChatWindow;
