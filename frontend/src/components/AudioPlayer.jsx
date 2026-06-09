function AudioPlayer({ audioUrl }) {
  return (
    <div>
      <h3>Generated Music</h3>

      <audio
        controls
        style={{ width: "100%" }}
        src={`http://127.0.0.1:8000${audioUrl}`}
      />

      <br />
      <br />

      <a
        href={`http://127.0.0.1:8000${audioUrl}`}
        download
      >
        Download Music
      </a>
    </div>
  );
}

export default AudioPlayer;