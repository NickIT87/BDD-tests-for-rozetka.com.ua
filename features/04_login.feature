Feature: fail login page

 Scenario Outline: Check login failure
    then after redirect on cart we login on shop <loginMail> and <password>
    when login fail we can see error message

 Examples: By login
    | loginMail      | password |
    | test@gmail.com | testpass |