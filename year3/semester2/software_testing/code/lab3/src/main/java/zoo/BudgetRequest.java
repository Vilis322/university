package zoo;

public class BudgetRequest {

    public enum Status { PENDING, GRANTED, DENIED }

    private final String applicant;
    private final String animalName;
    private final String statement;
    private final double requestedAmount;
    private Status status;
    private double grantedAmount;
    private String responseStatement;

    public BudgetRequest(String applicant, String animalName, String statement, double requestedAmount) {
        this.applicant = applicant;
        this.animalName = animalName;
        this.statement = statement;
        this.requestedAmount = requestedAmount;
        this.status = Status.PENDING;
    }

    public String getApplicant() {
        return applicant;
    }

    public String getAnimalName() {
        return animalName;
    }

    public String getStatement() {
        return statement;
    }

    public double getRequestedAmount() {
        return requestedAmount;
    }

    public Status getStatus() {
        return status;
    }

    public double getGrantedAmount() {
        return grantedAmount;
    }

    public String getResponseStatement() {
        return responseStatement;
    }

    public void grant(double amount) {
        this.status = Status.GRANTED;
        this.grantedAmount = amount;
    }

    public void deny(String responseStatement) {
        this.status = Status.DENIED;
        this.responseStatement = responseStatement;
    }
}
