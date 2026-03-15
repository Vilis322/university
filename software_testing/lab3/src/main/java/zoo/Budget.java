package zoo;

import java.util.ArrayList;
import java.util.List;

public class Budget {

    private final String animalName;
    private double totalBudget;
    private double spent;
    private final List<Order> pendingOrders = new ArrayList<>();
    private final List<BudgetRequest> requests = new ArrayList<>();

    public Budget(String animalName, double totalBudget) {
        this.animalName = animalName;
        this.totalBudget = totalBudget;
        this.spent = 0;
    }

    public String getAnimalName() {
        return animalName;
    }

    public double getTotalBudget() {
        return totalBudget;
    }

    public double getSpent() {
        return spent;
    }

    public double getReserved() {
        return pendingOrders.stream()
                .filter(o -> !o.isArrived())
                .mapToDouble(Order::getInvoiceTotal)
                .sum();
    }

    public double getRemaining() {
        return totalBudget - spent - getReserved();
    }

    public void addSpent(double amount) {
        this.spent += amount;
    }

    public void increaseBudget(double amount) {
        this.totalBudget += amount;
    }

    public void addPendingOrder(Order order) {
        pendingOrders.add(order);
    }

    public List<Order> getPendingOrders() {
        return pendingOrders;
    }

    public void addRequest(BudgetRequest request) {
        requests.add(request);
    }

    public List<BudgetRequest> getRequests() {
        return requests;
    }

    public boolean wouldExceedBudget(double orderTotal) {
        return orderTotal > getRemaining();
    }
}
