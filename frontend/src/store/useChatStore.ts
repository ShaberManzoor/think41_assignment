import { create } from "zustand";

interface Message {
  role: "user" | "assistant";
  content: string;
}

interface ChatStore {
  messages: Message[];
  loading: boolean;
  sessionId: string | null;
  setSessionId: (id: string) => void;
  addMessage: (msg: Message) => void;
  setMessages: (msgs: Message[]) => void;
  setLoading: (val: boolean) => void;
}

export const useChatStore = create<ChatStore>((set) => ({
  messages: [],
  loading: false,
  sessionId: null,
  setSessionId: (id) => set({ sessionId: id }),
  addMessage: (msg) => set((state) => ({ messages: [...state.messages, msg] })),
  setMessages: (msgs) => set({ messages: msgs }),
  setLoading: (val) => set({ loading: val }),
}));
