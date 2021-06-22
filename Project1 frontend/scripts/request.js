let spent_amount = 0
let req_amount = 0
let reim_reason = ""

const spentInput = document.getElementById("samount")
const reqInput = document.getElementById("ramount")
const reasonInput = document.getElementById("reim_reason")
spentInput.addEventListener('input', updateSpent)
reqInput.addEventListener('input', updateReq)
reasonInput.addEventListener('input', updateReason)

async function sub_reim(){
    const account_id = localStorage.getItem("accountID");    
    const response = await fetch(`http://localhost:5000/requests`, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'accountID': account_id
        },
        referrerPolicy: 'no-referrer',
        body: JSON.stringify({
            'amountSpent': spent_amount,
            'amountRequested': req_amount,
            'reason': reim_reason
        })
    });
    

    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        const jform = await response.json()
        window.location.href="employee_page.html"    
    }
}

function updateSpent(e){spent_amount = e.target.value;}
function updateReq(e){req_amount = e.target.value;}
function updateReason(e){reim_reason = e.target.value;}