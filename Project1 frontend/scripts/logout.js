async function log_out(){    
    const account_id = localStorage.getItem("accountID");
    console.log(account_id)
    const response = await fetch(`http://localhost:5000/logout`, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'accountID': account_id
        },
        body:{},
        referrerPolicy: 'no-referrer',
    });
    

    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        localStorage.removeItem("accountID");
        window.location.href="login.html"
    }
    

}

