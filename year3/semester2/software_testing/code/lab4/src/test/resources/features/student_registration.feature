Feature: Selenium Automation Practice Form
  Automating the Student Registration Form on tutorialspoint
  to verify that each form field can be filled programmatically
  via Selenium WebDriver, with the test flow defined in Gherkin.

  Scenario: Fill in and submit the Student Registration Form
    Given user launches the browser
    When user opens the student registration form page
    Then user enters the name "Jackie"
    And user enters the email "jackie.lin@example.com"
    And user selects the gender "Female"
    And user enters the mobile number "5551234567"
    And user enters the date of birth "01/15/2000"
    And user enters the subject "Software Testing"
    And user picks the hobbies "Sports, Reading"
    And user uploads a picture
    And user enters the current address "Narva mnt 25, Tartu, Estonia"
    And user submits the form
