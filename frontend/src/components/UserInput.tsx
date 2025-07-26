import React, { useState } from "react";
// import "./UserInput.css";

type Props = {
  onSend: (text: string) => void;
};

const UserInput: React.FC<Props> = ({ onSend }) => {
  const [text, setText] = useState<string>("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <form className="flex mt-4 gap-2" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Type your message..."
        className="flex-1 border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Send
      </button>
    </form>
  );
};

export default UserInput;
