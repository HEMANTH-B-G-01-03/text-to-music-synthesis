import { useState } from "react";
import API from "./services/api";

import PromptForm from "./components/PromptForm";
import AudioPlayer from "./components/AudioPlayer";

function App() {
  const [loading, setLoading] = useState(false);
  const [musicData, setMusicData] = useState(null);

  const generateMusic = async (prompt) => {
    try {
      setLoading(true);

      const response = await API.post("/generate", {
        prompt,
      });

      setMusicData(response.data);
    } catch (error) {
      console.error(error);
      alert("Music generation failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "50px auto",
        padding: "20px",
      }}
    >
      <h1>🎵 Text To Music Synthesis</h1>

      <PromptForm
        onGenerate={generateMusic}
        loading={loading}
      />

      {musicData && (
        <div style={{ marginTop: "30px" }}>
          <h3>Enhanced Prompt</h3>

          <p>{musicData.enhanced_prompt}</p>

          <AudioPlayer
            audioUrl={musicData.audio_url}
          />
        </div>
      )}
    </div>
  );
}

export default App;