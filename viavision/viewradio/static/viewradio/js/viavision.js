const audio = document.getElementById('radio-player');
const visualizer = document.getElementById('visualizer');

// Crear barras del visualizador
for (let i = 0; i < 20; i++) {
    const bar = document.createElement('div');
    bar.className = 'bar';
    bar.style.height = '4px';
    visualizer.appendChild(bar);
}

const bars = document.querySelectorAll('.bar');

// Animar según el estado del audio
setInterval(() => {
    if (!audio.paused) {
        bars.forEach(bar => {
            bar.style.height = Math.random() * 80 + 10 + 'px';
        });
    } else {
        bars.forEach(bar => bar.style.height = '4px');
    }
}, 100);

// Spotlight effect
document.addEventListener('mousemove', e => {
    document.body.style.setProperty('--x', e.clientX + 'px');
    document.body.style.setProperty('--y', e.clientY + 'px');
});