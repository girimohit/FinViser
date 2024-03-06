var ctx = document.getElementById("lineChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    datasets: [
      {
        label: "Savings in ₹",
        data: [2050, 1900, 2100, 2800, 1800, 2000, 2500, 2600, 2450, 1950, 2300, 2900],
        backgroundColor: ["rgba(85,85,85, 1)"],
        borderColor: "rgb(41, 155, 99)",
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
  },
});

let contestEndDate;
const totalTime = 24 * 60 * 60 * 1000; // Total time in milliseconds (1 day)

// Function to start the countdown

function startCountdown() {
  const startDateInput = document.getElementById("startDate").value;
  const endDateInput = document.getElementById("endDate").value;

  const startDate = new Date(startDateInput).getTime();
  const endDate = new Date(endDateInput).getTime();

  const daysBetween = Math.ceil((endDate - startDate) / (24 * 60 * 60 * 1000));

  if (daysBetween <= 0) {
    alert("End date must be after the start date.");
    return;
  }

  contestEndDate = endDate;
  updateChart();
}

// Get the canvas context

const ctx2 = document.getElementById("countdownTimer").getContext("2d");

// Initialize the chart
const myChart2 = new Chart(ctx2, {
  type: "doughnut",
  data: {
    labels: ["Time Passed", "Time Left"],
    datasets: [
      {
        data: [100, 0], // Initial data for the chart (time passed: 100%, time left: 0%)
        backgroundColor: ["rgba(255, 99, 132, 0.5)", "rgba(255, 255, 255, 0.5)"],
        borderColor: ["rgba(255, 99, 132, 1)", "rgba(255, 255, 255, 1)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
    cutoutPercentage: 80,
    animation: false, // Disable animation for better visualization
  },
});

// Function to update the chart
function updateChart() {
  const now = new Date().getTime();
  const timeLeft = Math.max(contestEndDate - now, 0); // Ensure timeLeft is non-negative
  const percentageLeft = (timeLeft / totalTime) * 100; // Calculate the percentage of time left

  myChart2.data.datasets[0].data = [100 - percentageLeft, percentageLeft];
  myChart2.update();
}

// Update the chart every minute
setInterval(() => {
  updateChart();
}, 60000);

// var ctx2 = document.getElementById('doughnut').getContext('2d');
// var myChart2 = new Chart(ctx2, {
//     type: 'doughnut',
//     data: {
//         labels: ['Academic', 'Non-Academic', 'Administration', 'Others'],
//         datasets: [{
//             label: 'Employees',
//             data: [42, 12, 8, 6],
//             backgroundColor: [
//                 'rgba(41, 155, 99, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(120, 46, 139,1)'
//             ],
//             borderColor: [
//                 'rgba(41, 155, 99, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(120, 46, 139,1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });
