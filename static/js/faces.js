async function fetchFaces() {
    try {
        const response = await fetch('/face_frames');
        return await response.json();
    } catch (error) {
        console.error("Error fetching face data:", error);
        return [];
    }
}

function drawFaceBoxes(faces) {
    const video = document.getElementById('video');
    const container = document.getElementById('video-container');

    const imgWidth = video.naturalWidth;
    const imgHeight = video.naturalHeight;
    const displayWidth = video.clientWidth;
    const displayHeight = video.clientHeight;

    const scaleX = displayWidth / imgWidth;
    const scaleY = displayHeight / imgHeight;

    document.querySelectorAll('.face-rect').forEach(box => box.remove());

    faces.forEach((face, i) => {
        const box = document.createElement('div');
        box.className = 'face-rect';

        // Scale coordinates
        box.style.left = (face.x * scaleX) + 'px';
        box.style.top = (face.y * scaleY) + 'px';
        box.style.width = (face.w * scaleX) + 'px';
        box.style.height = (face.h * scaleY) + 'px';

        box.onclick = () => {
            console.log(`Clicked face #${i}`);
            window.open(`/face/${i}`, '_blank');
        };

        container.appendChild(box);
    });
}


async function updateLoop() {
    while (true) {
        const faces = await fetchFaces();
        drawFaceBoxes(faces);
        await new Promise(resolve => setTimeout(resolve, 250));
    }
}

updateLoop();
