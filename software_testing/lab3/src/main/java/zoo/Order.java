package zoo;

import java.time.LocalDate;

public class Order {

    private final String dealerName;
    private final double invoiceTotal;
    private final LocalDate expectedDelivery;
    private boolean arrived;
    private LocalDate arrivalDate;

    public Order(String dealerName, double invoiceTotal, LocalDate expectedDelivery) {
        this.dealerName = dealerName;
        this.invoiceTotal = invoiceTotal;
        this.expectedDelivery = expectedDelivery;
        this.arrived = false;
    }

    public String getDealerName() {
        return dealerName;
    }

    public double getInvoiceTotal() {
        return invoiceTotal;
    }

    public LocalDate getExpectedDelivery() {
        return expectedDelivery;
    }

    public boolean isArrived() {
        return arrived;
    }

    public LocalDate getArrivalDate() {
        return arrivalDate;
    }

    public void markArrived(LocalDate date) {
        this.arrived = true;
        this.arrivalDate = date;
    }

    public boolean isOverdue(LocalDate currentDate) {
        return !arrived && currentDate.isAfter(expectedDelivery);
    }
}
