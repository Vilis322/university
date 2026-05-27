package stepdefinitions;

import io.cucumber.java.After;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import java.util.Arrays;

public class StudentRegistrationSteps {

    private static final String FORM_URL =
            "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php";

    private WebDriver driver;
    private WebDriverWait wait;

    @Given("user launches the browser")
    public void user_launches_the_browser() {
        ChromeOptions options = new ChromeOptions();
        if (Boolean.parseBoolean(System.getProperty("headless", "false"))) {
            options.addArguments("--headless=new");
        }
        options.addArguments("--window-size=1280,900");
        options.addArguments("--disable-notifications");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @When("user opens the student registration form page")
    public void user_opens_the_student_registration_form_page() {
        driver.get(FORM_URL);
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("name")));
    }

    @Then("user enters the name {string}")
    public void user_enters_the_name(String name) {
        WebElement nameInput = driver.findElement(By.id("name"));
        nameInput.clear();
        nameInput.sendKeys(name);
    }

    @And("user enters the email {string}")
    public void user_enters_the_email(String email) {
        WebElement emailInput = driver.findElement(By.id("email"));
        emailInput.clear();
        emailInput.sendKeys(email);
    }

    @And("user selects the gender {string}")
    public void user_selects_the_gender(String gender) {
        String xpath = String.format(
                "//input[@type='radio' and following-sibling::label[1][normalize-space()='%s']]",
                gender);
        driver.findElement(By.xpath(xpath)).click();
    }

    @And("user enters the mobile number {string}")
    public void user_enters_the_mobile_number(String mobile) {
        WebElement mobileInput = driver.findElement(By.id("mobile"));
        mobileInput.clear();
        mobileInput.sendKeys(mobile);
    }

    @And("user enters the date of birth {string}")
    public void user_enters_the_date_of_birth(String dob) {
        WebElement dobInput = driver.findElement(By.id("dob"));
        dobInput.sendKeys(dob);
    }

    @And("user enters the subject {string}")
    public void user_enters_the_subject(String subject) {
        WebElement subjectInput = driver.findElement(By.id("subjects"));
        subjectInput.clear();
        subjectInput.sendKeys(subject);
    }

    @And("user picks the hobbies {string}")
    public void user_picks_the_hobbies(String hobbies) {
        Arrays.stream(hobbies.split(","))
                .map(String::trim)
                .forEach(hobby -> {
                    String xpath = String.format(
                            "//input[@type='checkbox' and following-sibling::label[1][normalize-space()='%s']]",
                            hobby);
                    driver.findElement(By.xpath(xpath)).click();
                });
    }

    @And("user uploads a picture")
    public void user_uploads_a_picture() throws IOException {
        Path tempFile = Files.createTempFile("lab4-upload-", ".txt");
        Files.writeString(tempFile, "lab4 sample upload");
        driver.findElement(By.cssSelector("input[type='file']"))
                .sendKeys(tempFile.toAbsolutePath().toString());
    }

    @And("user enters the current address {string}")
    public void user_enters_the_current_address(String address) {
        WebElement addressInput = driver.findElement(By.cssSelector("textarea"));
        addressInput.clear();
        addressInput.sendKeys(address);
    }

    @And("user submits the form")
    public void user_submits_the_form() {
        WebElement submit = driver.findElement(By.cssSelector("input[type='submit']"));
        // The page has a sticky cookie/ads bar that can overlap the submit button,
        // so scroll the element into view and click via JS to bypass any overlay.
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].scrollIntoView({block: 'center'});", submit);
        js.executeScript("arguments[0].click();", submit);
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
