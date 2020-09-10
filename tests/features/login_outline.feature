@login-outline
Feature: Login
  As a user I want to login in the system,
  so I can access manage my account

  Background:
    Given  API endpoint for user login

  Scenario Outline: User Login with different inputs
    When  Required data for login are set "<email>","<password>"
    Then  POST request is made to endpoint with data provided
    And  Response message should be "<message>" and status code "<status_code>"

    Examples:
      | email           | password | status_code | message                                       |
      | valon@gmail.com | 123456   | 200         | ""                                            |
      | valon@gmail.com | 1234567  | 400         | Incorrect email or password                   |
      | valon@gmail.co  | 123456   | 400         | Incorrect email or password                   |
      |                 | 123456   | 422         | field required                                |
      | valon@gmail.com | 12345    | 421         | Password should contain at least 6 characters |
      | valon@gmail.com | 123456   | 200         | ""                                            |