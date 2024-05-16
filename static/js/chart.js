
// Create chart
const ctx = document.getElementById('rateChart').getContext('2d');
const gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, 'rgba(75, 192, 192, 0.7)'); // start color
gradient.addColorStop(1, 'rgba(75, 192, 192, 0.1)'); // end color

const rateChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
        datasets: [{
            label: selected_currency + ' Exchange Rate',
            data: rates,
            fill: true,
            backgroundColor: gradient,
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            pointRadius: 4,
            pointHoverRadius: 6,
            hitRadius: 10, // Set hit radius for each point
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Exchange Rate Chart',
                font: {
                    size: 18,
                    weight: 'bold'
                }
            },
            legend: {
                display: true,
                position: 'bottom',
                labels: {
                    font: {
                        size: 14
                    }
                }
            },
            tooltip: {
                enabled: true,
                mode: 'index',
                intersect: false,
            }
        },
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'day',
                    displayFormats: {
                        day: 'MMM dd'
                    }
                },
                title: {
                    display: true,
                    text: 'Date',
                    font: {
                        size: 14
                    }
                },
                ticks: {
                    font: {
                        size: 12
                    },
                    color: 'rgba(0, 0, 0, 0.7)' // axis label color
                },
                grid: {
                    display: true,
                    color: 'rgba(0, 0, 0, 0.1)'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Exchange Rate',
                    font: {
                        size: 14
                    }
                },
                ticks: {
                    font: {
                        size: 12
                    },
                    color: 'rgba(0, 0, 0, 0.7)' // axis label color
                },
                grid: {
                    display: true,
                    color: 'rgba(0, 0, 0, 0.1)'
                }
            }
        },
        elements: {
            line: {
                tension: 0.4, // adjust line curve
                shadowOffsetX: 3,
                shadowOffsetY: 3,
                shadowBlur: 10,
                shadowColor: 'rgba(75, 192, 192, 0.3)' // shadow color
            }
        },
        animation: {
            duration: 1000, // animation duration in milliseconds
            easing: 'easeInOutQuart' // easing function
        }
    }
});
