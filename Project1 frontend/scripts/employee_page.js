let pending_request_list = [];
let past_request_list = [];
let number_per_page = 2;
let pending_index = 0;
let past_index = 0;

const past = document.getElementById("past_req_container")
const pend = document.getElementById("pend_req_container")

function getReimbursementInnerHtml(reim, dom_id) {
    textColor = "u-color-yellow";
    statusText = "Pending";
    if (!reim.pending){
        if (reim.approved) {
            statusText = "Approved";
        }
        else {
            textColor = "u-color-red";
            statusText = "Denied";
        }
    }
   

    return `
    <div id="${dom_id}" style="border: 3px solid #ffffff;">
        <h2 class="u-margin-bottom-small">Request #${reim.requestId}</h2>
        <h2>Amount  spent: ${reim.amountSpent}</h2>
        <h2>Amount requested: ${reim.amountRequested}</h2>
        <h3>${reim.reason}</h3>
        <p text-decoration: underline overline; class="${textColor}">${statusText}</p>
        <h2 class="u-margin-bottom-small">${reim.response}</h2>
    </div>`
}

function get_all_innerhtml(Requests, index, dom_id){
    let final_html = ""
    let counter = 0
    for(let i=index* number_per_page; i < Requests.length; ++i){
        if (counter === number_per_page){
            break;
        }
        final_html += getReimbursementInnerHtml(Requests[i], dom_id + counter);
        ++ counter;
        
    }
    return final_html

}

function update_pending_reimbursement(){
    let innerHTML = get_all_innerhtml(pending_request_list, pending_index, "pend_reim_child_")
    innerHTML += `<div class="row">
        <div class="col-1-of-2 u-center-text">
            <button id="dec_pend_reim" onclick="update_pending_index(1)" type="button" class="btn">inc</button>
        </div>
        <div class="col-1-of-2 u-center-text">
            <button id="inc_pend_reim" onclick="update_pending_index(-1)" type="button" class="btn">dec</button>
        </div>
    </div>`
    pend.innerHTML=innerHTML

}
function update_past_reimbursement(){
    let innerHTML = get_all_innerhtml(past_request_list, past_index, "past_reim_child_")
    innerHTML += `<div class="row">
        <div class="col-1-of-2 u-center-text">
            <button id="dec_past_reim" onclick="update_past_index(1)" type="button" class="btn">inc</button>
        </div>
        <div class="col-1-of-2 u-center-text">
            <button id="inc_past_reim" onclick="update_past_index(-1)" type="button" class="btn">dec</button>
        </div>
    </div>`
    past.innerHTML=innerHTML
    
}

function update_pending_index(change){
    if (pending_index + change < 0){
        return
    }
    if ((pending_index * number_per_page) - number_per_page > pending_request_list.length){
        return
    }
    pending_index += change
    update_pending_reimbursement()
}

function update_past_index(change){
    if (past_index + change < 0){
        return
    }
    if ((past_index * number_per_page) - number_per_page > past_request_list.length){
        return
    }
    past_index += change
    update_past_reimbursement()
}
function new_request(){
    window.location.href="reimbursement_form.html"
}

async function get_user_requests(){
    const account_id = localStorage.getItem("accountID");    
    const response = await fetch(`http://localhost:5000/requests/user`, {
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
        for(let i = 0; i < jform.length; ++i) {
            if (jform[i].pending)
                pending_request_list.push(jform[i])
            else
                past_request_list.push(jform[i]) 
        }
        update_pending_reimbursement();
        update_past_reimbursement();
    }
}
get_user_requests()