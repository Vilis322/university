# *Lab 4 — Cucumber + Selenium WebDriver*

## *Description*
+ BDD-style automation of the **Student Registration Form** on
  `https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php`.
+ The scenario is described in Gherkin (`.feature` file) and executed by
  Java step definitions that drive a real Chrome browser via Selenium WebDriver.

## *Structure*
```
lab4/
├── pom.xml
├── README.md
└── src/test/
    ├── java/
    │   ├── runners/RunCucumberTest.java
    │   └── stepdefinitions/StudentRegistrationSteps.java
    └── resources/features/student_registration.feature
```

## *Requirements*
+ **Java 17** or higher.
+ **Maven 3.9+**.
+ **Google Chrome** installed locally (the matching `chromedriver` is fetched
  automatically by Selenium Manager, no manual driver download required).

## *Run*
```bash
# default — visible browser window
mvn test

# headless mode (no UI, useful for CI)
mvn test -Dheadless=true
```

## *Scenario*
The single scenario fills in every visible field of the form
(name, email, gender, mobile, date of birth, subject, hobbies,
picture upload, current address) and submits it.
