@web
Feature: Facebook login
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.


  Background:
    Given the Facebook home page is displayed

  Scenario: Basic DuckDuckGo Search
    When the user enters username and password
    Then user should see facebook home page

