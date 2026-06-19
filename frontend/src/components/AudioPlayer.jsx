// function AudioPlayer({ audioUrl }) {
//   return (
//     <div>
//       <h3>Generated Music</h3>

//       <audio
//         controls
//         style={{ width: "100%" }}
//         src={`http://127.0.0.1:8000${audioUrl}`}
//       />

//       <br />
//       <br />

//       <a
//         href={`http://127.0.0.1:8000${audioUrl}`}
//         download
//       >
//         Download Music
//       </a>
//     </div>
//   );
// }

// export default AudioPlayer;


function AudioPlayer({ audioUrl }) {
  return (
    <div className="audio-section">
      <audio
        controls
        src={`http://127.0.0.1:8000${audioUrl}`}
        className="audio-player"
      />

      <a
        href={`http://127.0.0.1:8000${audioUrl}`}
        download
        className="download-btn"
      >
        ⬇ Download Music
      </a>
    </div>
  );
}

export default AudioPlayer;