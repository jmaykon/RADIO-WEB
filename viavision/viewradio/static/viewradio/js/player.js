// player.js - Gestión de audio y metadatos
document.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById('audio-player');
    const playBtn = document.getElementById('main-play-btn');
    const playIcon = document.getElementById('play-icon');
    const songTitle = document.getElementById('current-song');
    const artistName = document.getElementById('current-artist');
    const albumArt = document.getElementById('player-album-art');
    const visualizer = document.getElementById('visualizer-mini');

    // CONFIGURACIÓN: Reemplaza con tu URL de streaming
    const STREAM_URL = "https://tu-servidor.com/stream"; 
    
    let isPlaying = false;

    // Función para cambiar el estado visual
    const updateUI = (status) => {
        if (status) {
            playIcon.setAttribute('data-lucide', 'pause');
            albumArt.classList.add('animate-spin-slow');
            visualizer.classList.remove('hidden');
        } else {
            playIcon.setAttribute('data-lucide', 'play');
            albumArt.classList.remove('animate-spin-slow');
            visualizer.classList.add('hidden');
        }
        if (window.lucide) lucide.createIcons();
    };

    // Función Play/Pause
    const togglePlayback = () => {
        if (audio.paused) {
            audio.src = STREAM_URL;
            audio.play()
                .then(() => {
                    isPlaying = true;
                    updateUI(true);
                    updateMetadata();
                })
                .catch(error => {
                    console.error("Error al reproducir stream:", error);
                    songTitle.innerText = "Error de conexión";
                });
        } else {
            audio.pause();
            audio.src = ""; // Detiene la descarga de datos
            isPlaying = false;
            updateUI(false);
        }
    };

    // Función para obtener metadatos (Simulada hasta tener tu URL real)
    const updateMetadata = async () => {
        if (!isPlaying) return;
        
        try {
            // Aquí podrías hacer un fetch a tu API de radio
            // const response = await fetch('URL_DE_TU_API');
            // const data = await response.json();
            
            // Simulación dinámica
            const mockSongs = [
                { t: "Ritmo Galáctico", a: "ViaVision Mix" },
                { t: "Cumbia Interestelar", a: "Retro Cumbia FM" }
            ];
            const pick = mockSongs[Math.floor(Math.random() * mockSongs.length)];

            songTitle.innerText = pick.t;
            artistName.innerText = pick.a;
        } catch (e) {
            console.log("Error actualizando metadatos");
        }
    };

    playBtn.addEventListener('click', togglePlayback);
    
    // Actualizar nombres cada 30 segundos si está sonando
    setInterval(updateMetadata, 30000);
});