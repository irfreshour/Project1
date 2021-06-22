let email = ""
let pw = ""

const emailInput = document.getElementById('email')
const pwInput = document.getElementById('pw')
emailInput.addEventListener('input', updateEmail)
pwInput.addEventListener('input', updatePw)

async function log_in(){    
    const response = await fetch(`http://localhost:5000/login`, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        referrerPolicy: 'no-referrer',
        body: JSON.stringify({
            'email': email,
            'password': pw
        })
    });
    

    if (!response.ok){
        let text = await response.text();
        console.log(text);
    }else{
        const jform = await response.json()
        localStorage.setItem("accountID", jform.accountID)
        if (jform.manager){
            window.location.href="manager_page.html"
        }else{
            window.location.href="employee_page.html"    
        }
    }


}
function updateEmail(e){email = e.target.value;}

function updatePw(e){pw = e.target.value;}