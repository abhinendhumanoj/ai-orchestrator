import React, { useState } from "react";
import axios from "axios";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { role: "assistant", text: "Hello! How can I help you today?" },
  ]);
  const [loading, setLoading] = useState(false);

  // ✅ Automatically choose between local and deployed backend
  const isLocal = window.location.hostname === "localhost";
  const API_URL = isLocal
    ? "http://127.0.0.1:8000/api/orchestrate"
    : "https://ai-orchestrator-backend-ibmx.onrender.com/api/orchestrate";


  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", text: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      // ✅ Send correct field expected by FastAPI
      const response = await axios.post(API_URL, {
        user_message: input,
      });

      const reply =
        response.data.answer ||
        response.data.response ||
        "Sorry, I couldn’t get a reply from the AI.";

      setMessages([...newMessages, { role: "assistant", text: reply }]);
    } catch (error) {
      console.error("❌ Error connecting to backend:", error);
      setMessages([
        ...newMessages,
        { role: "assistant", text: "⚠️ Error connecting to backend." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "Arial, sans-serif",
        maxWidth: "800px",
        margin: "0 auto",
      }}
    >
      <h1 style={{ textAlign: "center", color: "#2c3e50" }}>
        AI Tutor Orchestrator
      </h1>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "15px",
          height: "400px",
          overflowY: "auto",
          borderRadius: "8px",
          backgroundColor: "#f9f9f9",
        }}
      >
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: "10px" }}>
            <strong
              style={{
                color: msg.role === "user" ? "#2980b9" : "#27ae60",
              }}
            >
              {msg.role === "user" ? "You" : "AI Tutor"}:
            </strong>{" "}
            {msg.text}
          </div>
        ))}

        {loading && <p style={{ color: "#999" }}>⏳ Thinking...</p>}
      </div>

      <div
        style={{
          marginTop: "15px",
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question..."
          style={{
            flex: 1,
            padding: "10px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          style={{
            marginLeft: "10px",
            padding: "10px 15px",
            borderRadius: "5px",
            backgroundColor: "#27ae60",
            color: "white",
            border: "none",
            cursor: "pointer",
          }}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
}

export default App;
