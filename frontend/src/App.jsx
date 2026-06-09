// 





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
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid #ddd",
            borderRadius: "12px",
            backgroundColor: "#f9f9f9",
          }}
        >
          <h2>🎵 Generated Music</h2>

          <AudioPlayer
            audioUrl={musicData.audio_url}
          />

          <h3 style={{ marginTop: "20px" }}>
            ✨ Enhanced Prompt
          </h3>

          <p>{musicData.enhanced_prompt}</p>

          <h3 style={{ marginTop: "20px" }}>
            🎧 Similar Songs
          </h3>

          {musicData.recommendations &&
          musicData.recommendations.length > 0 ? (
            <ul
              style={{
                paddingLeft: "20px",
              }}
            >
              {musicData.recommendations.map(
                (song, index) => (
                  <li
                    key={index}
                    style={{
                      marginBottom: "12px",
                    }}
                  >
                    <a
                      href={song.youtube_url}
                      target="_blank"
                      rel="noreferrer"
                      style={{
                        textDecoration: "none",
                        color: "#1976d2",
                        fontWeight: "500",
                      }}
                    >
                      ▶ {song.title}
                    </a>
                  </li>
                )
              )}
            </ul>
          ) : (
            <p>No recommendations found.</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;