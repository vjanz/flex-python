@login
Feature: Login
  As a user I want to login in the system,
  so I can access manage my account

  Background:
    Given  API endpoint for user login
    Given  User is registered in system

  Scenario: Login with correct credentials
    When   Required data for login are set
    And    POST Request is made to login endpoint with specified data
    Then   Response status code should be 200


  Scenario: Login and get access token
    When   Required data for login are set
    And    POST Request is made to login endpoint with specified data
    Then   Response should contain access_token
    And    Response status code should be 200