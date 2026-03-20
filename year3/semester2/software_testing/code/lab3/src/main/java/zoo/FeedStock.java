package zoo;

import java.time.LocalDate;

public class FeedStock {

    private final String feedName;
    private final String animalName;
    private double quantity;
    private final LocalDate expirationDate;

    public FeedStock(String feedName, String animalName, double quantity, LocalDate expirationDate) {
        this.feedName = feedName;
        this.animalName = animalName;
        this.quantity = quantity;
        this.expirationDate = expirationDate;
    }

    public String getFeedName() {
        return feedName;
    }

    public String getAnimalName() {
        return animalName;
    }

    public double getQuantity() {
        return quantity;
    }

    public LocalDate getExpirationDate() {
        return expirationDate;
    }

    public boolean isExpired(LocalDate currentDate) {
        return currentDate.isAfter(expirationDate);
    }

    public void addQuantity(double amount) {
        this.quantity += amount;
    }
}
