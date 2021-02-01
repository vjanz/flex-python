@users
Feature: Users
  As a user I need to be logged in ,
  so I can make changes or see my personal account

  Scenario: Get the user that is logged in
    Given User is logged in
    Given API endpoint /api/v1/users/me
    When  POST Request is made to the specified endpoint with access_token in request header
    Then  Response should contain email,full_name,and id of current logged user



