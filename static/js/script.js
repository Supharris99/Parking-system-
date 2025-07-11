// Contoh skrip AJAX untuk deteksi motor
document.querySelector('button').addEventListener('click', async () => {
    try {
        const response = await fetch('/api/detect_plate');
        const data = await response.json();
        console.log(data);

        // Update informasi pemilik di halaman
        document.getElementById('owner-info').innerHTML = `
            <strong>Nama:</strong> ${data.name}<br>
            <strong>NIM:</strong> ${data.nim}<br>
            <strong>Jurusan:</strong> ${data.major}<br>
            <strong>No HP:</strong> ${data.phone}
        `;
    } catch (error) {
        console.error('Error:', error);
    }
});