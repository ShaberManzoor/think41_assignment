import React from "react";
import Message from "./Message";

type MessageProps = {
  messages: {
    sender: "user" | "ai";
    text: string;
  }[];
};

const MessageList: React.FC<MessageProps> = ({ messages }) => {
  return (
    <div className="message-list">
      {messages.map((msg, index) => (
        <Message key={index} sender={msg.sender} text={msg.text} />
      ))}
    </div>
  );
};

export default MessageList;
