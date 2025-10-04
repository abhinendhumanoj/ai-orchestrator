import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [userMessage, setUserMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null); // NEW

  // Auto-scroll when chat updates
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat, loading]); // Runs every time chat changes or loading changes

  const sendMessage = async () => {
    if (!userMessage.trim()) return;

    const newChat = [...chat, { role: "user", content: userMessage }];
    setChat(newChat);
    setLoading(true);

    try {
      const response = await axios.post("https://ai-orchestrator-backend.onrender.com/api/orchestrate", {
      query: input,
    });

      setChat([
        ...newChat,
        { role: "assistant", content: res.data.answer, mode: res.data.detected_mode }
      ]);
    } catch (err) {
      setChat([...newChat, { role: "assistant", content: "⚠️ Error connecting to backend." }]);
    }

    setLoading(false);
    setUserMessage("");
  };

  return (
    <div className="App">
      <h2>AI Tutor Orchestrator</h2>
      <div className="chat-box">
        {chat.map((msg, i) => (
          <div key={i} className={msg.role}>
            <b>{msg.role === "user" ? "You" : `AI (${msg.mode || "assistant"})`}:</b> {msg.content}
          </div>
        ))}

        {loading && (
          <div className="assistant typing">AI is typing...</div>
        )}

        {/* Invisible div to scroll into view */}
        <div ref={chatEndRef} />
      </div>

      <div className="input-area">
        <input
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          placeholder="Type your question..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
