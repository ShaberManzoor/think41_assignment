export default function Message({
  role,
  content,
}: {
  role: "user" | "assistant";
  content: string;
}) {
  const isUser = role === "user";
  return (
    <div
      className={`p-3 rounded-xl max-w-xl ${
        isUser ? "ml-auto bg-blue-100" : "mr-auto bg-white"
      }`}
    >
      <p className="text-sm text-gray-800">{content}</p>
    </div>
  );
}
