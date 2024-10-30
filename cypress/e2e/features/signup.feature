Feature: Create Account  for  new user

Background:
     Given Launch the URL

Scenario: Verify user can able to create the account and verify the success message

  And click on CreateAccount
  When user Fills all the mandatory fields
  And click on CreateAccount button
  Then Verify the success message

  Scenario: Verify user can able to signin to application

  Then Enter username and password
  And  click on signin button 
  And  verify application should get open



   