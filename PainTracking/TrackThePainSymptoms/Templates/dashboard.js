document.querySelectorAll('.sidebar a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetSection = document.querySelector(this.getAttribute('href'));
        targetSection.scrollIntoView({ behavior: 'smooth' });
    });
});

const painSlider = document.getElementById('pain-slider');
const painLevel = document.getElementById('pain-level');

painSlider.addEventListener('input', () => {
    painLevel.textContent = painSlider.value;
});


document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('painChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Pain Level',
                data: [4, 6, 5, 7, 8, 6, 5],
                borderColor: '#5a9',
                borderWidth: 2,
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true },
                x: { title: { display: true, text: 'Day of the Week' } }
            }
        }
    });
});