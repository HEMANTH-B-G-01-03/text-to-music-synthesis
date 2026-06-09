// import { useState } from "react";

// function PromptForm({ onGenerate, loading }) {
//   const [prompt, setPrompt] = useState("");

//   const handleSubmit = () => {
//     if (!prompt.trim()) return;

//     onGenerate(prompt);
//   };

//   return (
//     <div>
//       <input
//         type="text"
//         placeholder="Enter music prompt..."
//         value={prompt}
//         onChange={(e) => setPrompt(e.target.value)}
//         style={{
//           width: "100%",
//           padding: "12px",
//           marginBottom: "10px",
//         }}
//       />

//       <button onClick={handleSubmit}>
//         {loading ? "Generating..." : "Generate Music"}
//       </button>
//     </div>
//   );
// }

// export default PromptForm;



import { useState } from "react";

function PromptForm({ onGenerate, loading }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = () => {
    if (!prompt.trim()) return;

    onGenerate(prompt);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "10px",
      }}
    >
      <input
        type="text"
        placeholder="Enter music prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={handleKeyDown}
        style={{
          width: "100%",
          padding: "14px",
          borderRadius: "8px",
          border: "1px solid #ccc",
          fontSize: "16px",
        }}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        style={{
          padding: "12px",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          fontSize: "16px",
          backgroundColor: "#1976d2",
          color: "white",
        }}
      >
        {loading ? "Generating..." : "Generate Music"}
      </button>
    </div>
  );
}

export default PromptForm;