Feature: employee can post reimbursement requests

  Scenario Outline: employee logs in
    Given user is on the login page
    When user clicks on email input
    When user types <email> in the email input
    When user clicks on password input
    When user types <password> into password input
    When user presses submit button
    Then user is on the employee page
    When user click on the logout button on the employee page
    Then user arrives at the login page

    Examples:
      | email | password |
      | blah@blah.com | thepass |
