let pending_request_list = [];
let past_request_list = [];
let number_per_page = 2;
let pending_index = 0;
let past_index = 0;
let current_pend_index = -1
let approval = true

const past = document.getElementById("past_req_container")
const pend = document.getElementById("pend_req_container")
const reim_title = document.getElementById("reim_title")
const update_button = document.getElementById("submit_button")
const approval_check = document.getElementById("aradio")
const rejection_check = document.getElementById("rradio")
const responsive = document.getElementById("reim_response")

approval_check.addEventListener("click", () => {approval = true; console.log(approval);})
rejection_check.addEventListener("click", () => {approval = false; console.log(approval);})
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
        <p class="u-margin-bottom-small">${reim.response}</p>
    </div>`
}

function getPendingReimbursementInnerHtml(reim, dom_id, index) {
    textColor = "u-color-yellow";
    statusText = "Pending";
    if (!reim.pending){
        if (reim.approved) {
            textColor = "u-color-green";
            statusText = "Approved";
        }
        else {
            textColor = "u-color-red";
            statusText = "Denied";
        }
    }


    return `
    <div id="${dom_id}" onclick="set_pending_reim(${index})" style="border: 3px solid #ffffff;">
        <h2 class="u-margin-bottom-small">Request #${reim.requestId}</h2>
        <h2>Amount spent: ${reim.amountSpent}</h2>
        <h2>Amount requested: ${reim.amountRequested}</h2>
        <h3>${reim.reason}</h3>
        <p class="${textColor}">${statusText}</p>
        <p class="u-margin-bottom-small">${reim.response}</p>
    </div>`
}

function get_all_innerhtml(Requests, index, dom_id, reim_func){
    let final_html = ""
    let counter = 0
    for(let i=index* number_per_page; i < Requests.length; ++i){
        if (counter === number_per_page){
            break;
        }
        final_html += reim_func(Requests[i], dom_id + counter, i);
        ++ counter;
        
    }
    return final_html

}

function update_pending_reimbursement(){
    let innerHTML = get_all_innerhtml(pending_request_list, pending_index, "pend_reim_child_", getPendingReimbursementInnerHtml);
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
    let innerHTML = get_all_innerhtml(past_request_list, past_index, "past_reim_child_", getReimbursementInnerHtml)
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
function set_pending_reim(index){
    current_pend_index = index;
    if (current_pend_index === -1){
        reim_title.innerText = "";
        update_button.disabled = true;
    }else{
        reim_title.innerText = "Request #" + pending_request_list[index].requestId;
        update_button.disabled=false;
    } 
}

function set_past_reim(index){
    current_past_index = index;
    if (current_past_index === -1){
        reim_title.innerText = "";
        update_button.disabled = true;
    }else{
        reim_title.innerText = "Request #" + past_request_list[index].requestId;
        update_button.disabled=false;
    } 
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

async function update_request(){
    if(current_pend_index === -1){
        return
    }
    const reim = pending_request_list[current_pend_index];
    const account_id = localStorage.getItem("accountID");    
    const response = await fetch(`http://localhost:5000/requests/update`, {
        method: 'PUT',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'accountID': account_id
        },
        referrerPolicy: 'no-referrer',
        body: JSON.stringify({ 
            'requestId': reim.requestId,
            'accountId': reim.accountId,
            'amountSpent': reim.amountSpent,
            'amountRequested': reim.amountRequested,
            'reason': reim.reason,
            'pending': false,
            'approved': approval,
            'response': responsive.value
        })
    });
    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        pending_request_list.splice(current_pend_index, 1);
        reim.pending = false;
        reim.approved = approval;
        reim.response = responsive.value;
        past_request_list.push(reim);
        pending_index = 0;
        past_index = 0;
        update_pending_reimbursement();
        update_past_reimbursement();
        set_pending_reim(-1);
    } 
}
function view_statistics(){
    window.location.href="statistics.html"
}
get_user_requests()