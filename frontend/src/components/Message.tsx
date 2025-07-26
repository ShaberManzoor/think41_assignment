import React from "react";
// import "./Message.css";

type Props = {
  sender: "user" | "ai";
  text: string;
};

const Message: React.FC<Props> = ({ sender, text }) => {
  const isUser = sender === "user";

  return (
    <div className={`flex mb-2 ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-xs p-3 rounded-lg ${
          isUser ? "bg-blue-500 text-white" : "bg-gray-200 text-black"
        }`}
      >
        {text}
      </div>
    </div>
  );
};

export default Message;
