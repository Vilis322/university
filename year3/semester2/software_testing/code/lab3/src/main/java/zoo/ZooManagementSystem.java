package zoo;

import java.time.LocalDate;
import java.util.*;

public class ZooManagementSystem {

    private final Map<String, Budget> animalBudgets = new HashMap<>();
    private final Map<String, Set<String>> zookeeperAssignments = new HashMap<>();
    private final Set<String> authorizedDealers = new HashSet<>();
    private final List<FeedStock> feedStock = new ArrayList<>();
    private final List<String> messages = new ArrayList<>();

    // --- Dealer management ---

    public void addAuthorizedDealer(String dealer) {
        authorizedDealers.add(dealer);
    }

    public void removeAuthorizedDealer(String dealer) {
        authorizedDealers.remove(dealer);
    }

    public boolean isDealerAuthorized(String dealer) {
        return authorizedDealers.contains(dealer);
    }

    // --- Budget management ---

    public void createBudget(String animalName, double totalBudget) {
        animalBudgets.put(animalName, new Budget(animalName, totalBudget));
    }

    public Budget getBudget(String animalName) {
        return animalBudgets.get(animalName);
    }

    // --- Zookeeper assignments ---

    public void assignZookeeper(String zookeeper, String animalName) {
        zookeeperAssignments
                .computeIfAbsent(zookeeper, k -> new HashSet<>())
                .add(animalName);
    }

    public boolean isZookeeperAssigned(String zookeeper, String animalName) {
        Set<String> animals = zookeeperAssignments.get(zookeeper);
        return animals != null && animals.contains(animalName);
    }

    public Set<String> getAssignedAnimals(String zookeeper) {
        return zookeeperAssignments.getOrDefault(zookeeper, Collections.emptySet());
    }

    public Set<String> getZookeepersForAnimal(String animalName) {
        Set<String> keepers = new HashSet<>();
        for (var entry : zookeeperAssignments.entrySet()) {
            if (entry.getValue().contains(animalName)) {
                keepers.add(entry.getKey());
            }
        }
        return keepers;
    }

    // --- Budget viewing with access control ---

    public Budget viewBudget(String zookeeper, String animalName) {
        if (!isZookeeperAssigned(zookeeper, animalName)) {
            throw new SecurityException(
                    "Zookeeper " + zookeeper + " is not assigned to " + animalName);
        }
        return getBudget(animalName);
    }

    // --- Order management ---

    public Order placeOrder(String zookeeper, String animalName, String dealer,
                            double invoiceTotal, LocalDate expectedDelivery) {
        if (!isZookeeperAssigned(zookeeper, animalName)) {
            throw new SecurityException(
                    "Zookeeper " + zookeeper + " is not assigned to " + animalName);
        }
        if (!isDealerAuthorized(dealer)) {
            throw new IllegalArgumentException(
                    "Dealer " + dealer + " is not on the authorized dealers list.");
        }

        Budget budget = getBudget(animalName);
        Order order = new Order(dealer, invoiceTotal, expectedDelivery);
        budget.addPendingOrder(order);
        return order;
    }

    public void confirmDelivery(Order order, LocalDate arrivalDate,
                                String feedName, double quantity, LocalDate expirationDate) {
        order.markArrived(arrivalDate);

        String animalName = findAnimalForOrder(order);
        if (animalName != null) {
            Budget budget = getBudget(animalName);
            budget.addSpent(order.getInvoiceTotal());
            feedStock.add(new FeedStock(feedName, animalName, quantity, expirationDate));
        }
    }

    // --- Budget request management ---

    public BudgetRequest requestBudgetIncrease(String zookeeper, String animalName,
                                               String statement, double amount) {
        if (!isZookeeperAssigned(zookeeper, animalName)) {
            throw new SecurityException(
                    "Zookeeper " + zookeeper + " is not assigned to " + animalName);
        }

        Budget budget = getBudget(animalName);
        BudgetRequest request = new BudgetRequest(zookeeper, animalName, statement, amount);
        budget.addRequest(request);
        messages.add("Budget increase request from " + zookeeper
                + " for " + animalName + ": " + statement);
        return request;
    }

    public void grantRequest(BudgetRequest request, double grantedAmount) {
        request.grant(grantedAmount);

        Budget budget = getBudget(request.getAnimalName());
        budget.increaseBudget(grantedAmount);

        Set<String> keepers = getZookeepersForAnimal(request.getAnimalName());
        for (String keeper : keepers) {
            messages.add("To " + keeper + ": Budget increase of " + grantedAmount
                    + " granted for " + request.getAnimalName()
                    + ". Additional funds granted on request.");
        }
    }

    public void denyRequest(BudgetRequest request, String responseStatement) {
        request.deny(responseStatement);

        messages.add("To " + request.getApplicant()
                + ": Budget increase request denied for " + request.getAnimalName()
                + ". Reason: " + responseStatement);
    }

    // --- Feed stock ---

    public List<FeedStock> getStockForAnimal(String animalName) {
        return feedStock.stream()
                .filter(s -> s.getAnimalName().equals(animalName))
                .toList();
    }

    public List<FeedStock> getExpiredStock(String animalName, LocalDate currentDate) {
        return feedStock.stream()
                .filter(s -> s.getAnimalName().equals(animalName))
                .filter(s -> s.isExpired(currentDate))
                .toList();
    }

    // --- Messages ---

    public List<String> getMessages() {
        return Collections.unmodifiableList(messages);
    }

    // --- Helpers ---

    private String findAnimalForOrder(Order order) {
        for (var entry : animalBudgets.entrySet()) {
            if (entry.getValue().getPendingOrders().contains(order)) {
                return entry.getKey();
            }
        }
        return null;
    }
}
