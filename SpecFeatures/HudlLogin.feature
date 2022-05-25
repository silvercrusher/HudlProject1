# Created by md.islam at 5/25/2022
Feature: # Enter feature name here
  # Enter feature description here

  @login
    # Enter scenario name here
  Scenario: Coach_I can customize number of field entries displayed on the screen
    # Enter steps here
	Given I am logged in my view as "Coach_1"
	And I navigate to "Account Settings" page
	When I select Language in Account Preference
	Then I will randomly choose one options in dropdown