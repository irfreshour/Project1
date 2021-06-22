google.charts.load('current', { 'packages': ['corechart'] });
let employeeReqMoney = [];
let average_money_spent = 0;

function drawChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Employee');
    data.addColumn('number', 'Amount');
    data.addRows(employeeReqMoney);

    var options = {
        title: 'How Much Money Employees Spend',
        backgroundColor: 'transparent',
        width: 400,
        height: 300,
        is3D: true

    };

    var chart = new google.visualization.PieChart(document.getElementById('emp_money_container'));
    chart.draw(data, options);
}

async function get_user_requests(){
    const account_id = localStorage.getItem("accountID");    
    const response = await fetch(`http://localhost:5000/requests/all`, {
        method: 'GET',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'accountID': account_id
        },
        referrerPolicy: 'no-referrer',
    });
    

    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        const jform = await response.json();
        employeeToMoney = new Map()
        for(let i = 0; i < jform.length; ++i) {

            average_money_spent += jform[i].amountRequested;
            if (!employeeToMoney.has(jform[i].accountId)) {
                const got_user = await get_user(jform[i].accountId);
                console.log(got_user);
                employeeToMoney.set(jform[i].accountId, employeeReqMoney.length);
                employeeReqMoney.push([JSON.stringify(got_user), 0]);
            }
            else {
                employeeReqMoney[employeeToMoney.get(jform[i].accountId)][1] += jform[i].amountRequested;
            }
    
        }
        average_money_spent /= jform.length;
        document.getElementById("aver").innerText = "Average money reimbursed: " + average_money_spent
    }
}

async function get_user(user_id){
    const account_id = localStorage.getItem("accountID");    
    const response = await fetch(`http://localhost:5000/account/${user_id}`, {
        method: 'GET',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'accountID': account_id
        },
        referrerPolicy: 'no-referrer',
    });
    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        let user = await response.json();
        return user.userName;
    }
}

async function get_stats(){
    await get_user_requests();
    google.charts.setOnLoadCallback(drawChart);
}

get_stats();

