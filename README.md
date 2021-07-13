# Project1

# Project Description
An application meant to allow employees to sign in to submit reimbursement request for work-based expenses, and allows managers to confirm or deny requests at their own discretion.

# API endpoints
- POST: "/login": Checks credentials and attempts to log in the user
- POST: "/logout": Logs out a user that is currently logged in
- POST: "/requests": Allows user to submit a request to the database
- GET: "/account/<user_id>": Retrieves a user by their id
- GET: "/requests/user": Gets all requests made by a certain user
- GET: "/requests/all": Gets all requests made by any user
- PUT: "/requests/update": Updates the information of a given request, such as marking a reviewed request as approved or rejected
