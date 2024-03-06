

// Sample debt data
const debts = [
    { name: 'Credit Card', amount: 5000, dueDate: '2026-06-30' },
    { name: 'Student Loan', amount: 8000, dueDate: '2026-07-15' },
    { name: 'Applicance Loan', amount:10000, dueDate:'2024-07-15'},
    {name:"Car Loan", amount:15000,dueDate:'2024-05-07'}
    // Add more debt items as needed
];

// Function to render debt list
function renderDebts(debts) {
    const debtList = document.getElementById('debtList');
    debtList.innerHTML = '';
    debts.forEach(debt => {
        const debtItem = document.createElement('div');
        debtItem.classList.add('debt-item');
        debtItem.innerHTML = `
            <h3>${debt.name}</h3>
            <p>Amount: $${debt.amount}</p>
            <p>Due Date: ${debt.dueDate}</p>
        `;
        debtList.appendChild(debtItem);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    renderChart(debts);
});

// Function to render chart
function renderChart(debts) {
    const ctx = document.getElementById('chart').getContext('2d');
    const labels = debts.map(debt => debt.name);
    const amounts = debts.map(debt => debt.amount);

    const colors = [
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)'
    ];

    const chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Debt Amount',
                data: amounts,
                backgroundColor: colors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true
        }
    });
}




// Function to sort debts
function sortDebts(field) {
    debts.sort((a, b) => (a[field] > b[field]) ? 1 : -1);
    renderDebts(debts);
    renderChart(debts);
}

// Function to filter debts
function filterDebts(query) {
    const filteredDebts = debts.filter(debt => debt.name.toLowerCase().includes(query.toLowerCase()));
    renderDebts(filteredDebts);
    renderChart(filteredDebts);
}

// Event listeners for sorting and filtering
document.getElementById('sort').addEventListener('change', function() {
    const selectedField = this.value;
    sortDebts(selectedField);
});

document.getElementById('search').addEventListener('input', function() {
    const query = this.value;
    filterDebts(query);
});

// Initial render
renderDebts(debts);
render