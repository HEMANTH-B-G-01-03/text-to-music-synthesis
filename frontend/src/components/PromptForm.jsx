import { useState } from "react";

function PromptForm({ onGenerate, loading }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = () => {
    if (!prompt.trim()) return;

    onGenerate(prompt);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter music prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "10px",
        }}
      />

      <button onClick={handleSubmit}>
        {loading ? "Generating..." : "Generate Music"}
      </button>
    </div>
  );
}

export default PromptForm;