Feature: Register
  As a user I want to register in the system,
  so I can access features of the platform

  Background:
    Given API endpoint for user registration

  @correct-credentials
  Scenario: User Registration with correct credentials
    When  Required data for registration are set
    And   POST request is made to endpoint with specified data
    Then  Response status code should be 200
    And   The response body should contain id, email and hashed_password

  @wrong-credentials
  Scenario: User Registration with wrong credentials
    When  Data for registration don't fit the requirement fields
    And   POST request is made to endpoint with bad body request
    Then  Response status code should be 422

  @exist
  Scenario: User exist while trying to register
    When  Data for a user that is already registered is set
    And   POST Request is made to endpoint with those data
    Then  Response status code should be 400






