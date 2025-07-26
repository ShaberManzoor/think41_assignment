import { create } from "zustand";

type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

type ChatState = {
  messages: Message[];
  input: string;
  loading: boolean;
  sessionId: string | null;
  history: { sessionId: string; createdAt: string }[];

  setInput: (val: string) => void;
  addMessage: (msg: Message) => void;
  setLoading: (val: boolean) => void;
  setSessionId: (id: string) => void;
  setMessages: (msgs: Message[]) => void;
  setHistory: (items: { sessionId: string; createdAt: string }[]) => void;
};

export const useChatStore = create<ChatState>((set) => ({
  messages: [],
  input: "",
  loading: false,
  sessionId: null,
  history: [],

  setInput: (val) => set({ input: val }),
  addMessage: (msg) => set((state) => ({ messages: [...state.messages, msg] })),
  setLoading: (val) => set({ loading: val }),
  setSessionId: (id) => set({ sessionId: id }),
  setMessages: (msgs) => set({ messages: msgs }),
  setHistory: (items) => set({ history: items }),
}));
