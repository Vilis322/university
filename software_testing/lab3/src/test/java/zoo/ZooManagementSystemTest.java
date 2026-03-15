package zoo;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ZooManagementSystemTest {

    private ZooManagementSystem system;

    @BeforeEach
    void setUp() {
        system = new ZooManagementSystem();
        system.addAuthorizedDealer("FeedCo");
        system.addAuthorizedDealer("AnimalFoods Ltd");
        system.createBudget("Lion", 1000.0);
        system.createBudget("Elephant", 2000.0);
        system.assignZookeeper("Alice", "Lion");
        system.assignZookeeper("Alice", "Elephant");
        system.assignZookeeper("Bob", "Elephant");
    }

    // ==================================================================================
    // USER STORY 1: View Budget Breakdown
    //
    // Title: View animal feed budget breakdown
    // Priority: High
    // Estimate: 3 story points
    //
    // As a zookeeper,
    // I want to view the budget breakdown for my animal
    //     (total budget, amount spent, amount reserved, amount remaining),
    // so that I can plan future feed orders within the available budget.
    // ==================================================================================
    @Nested
    @DisplayName("US1: View animal feed budget breakdown")
    class UserStory1_ViewBudget {

        @Test
        @DisplayName("AC1: Given a zookeeper assigned to an animal with a monthly budget, " +
                "When the zookeeper views the budget, " +
                "Then the system shows total, spent, reserved, and remaining amounts")
        void ac1_viewBudgetBreakdown() {
            // Given
            Budget budget = system.getBudget("Lion");
            system.placeOrder("Alice", "Lion", "FeedCo", 200.0,
                    LocalDate.of(2026, 3, 20));

            // When
            Budget viewed = system.viewBudget("Alice", "Lion");

            // Then
            assertEquals(1000.0, viewed.getTotalBudget());
            assertEquals(0.0, viewed.getSpent());
            assertEquals(200.0, viewed.getReserved());
            assertEquals(800.0, viewed.getRemaining());
        }

        @Test
        @DisplayName("AC2: Given an animal has pending feed orders, " +
                "When the zookeeper views the budget, " +
                "Then pending orders are shown as reserved and not deducted from spent")
        void ac2_pendingOrdersAreReservedNotSpent() {
            // Given
            Order order = system.placeOrder("Alice", "Lion", "FeedCo", 300.0,
                    LocalDate.of(2026, 3, 25));

            // When
            Budget budget = system.viewBudget("Alice", "Lion");

            // Then
            assertEquals(0.0, budget.getSpent(), "Pending order should not be counted as spent");
            assertEquals(300.0, budget.getReserved(), "Pending order should be reserved");
            assertFalse(order.isArrived());
        }

        @Test
        @DisplayName("AC3: Given a zookeeper is NOT assigned to an animal, " +
                "When they try to view that animal's budget, " +
                "Then access is denied")
        void ac3_accessDeniedForUnassignedZookeeper() {
            // Given
            // Bob is not assigned to Lion

            // When / Then
            SecurityException ex = assertThrows(SecurityException.class,
                    () -> system.viewBudget("Bob", "Lion"));
            assertTrue(ex.getMessage().contains("not assigned"));
        }
    }

    // ==================================================================================
    // USER STORY 2: Order Feed from Authorized Dealer
    //
    // Title: Order feed and record invoice
    // Priority: High
    // Estimate: 5 story points
    //
    // As a zookeeper,
    // I want to order feed from an authorized dealer and record the invoice total
    //     with an expected delivery date,
    // so that the order is tracked and the budget is properly reserved.
    // ==================================================================================
    @Nested
    @DisplayName("US2: Order feed and record invoice")
    class UserStory2_OrderFeed {

        @Test
        @DisplayName("AC1: Given a zookeeper responsible for an animal and the order " +
                "does not exceed the budget, " +
                "When they place an order with an authorized dealer, " +
                "Then the order is recorded and the amount is reserved in the budget")
        void ac1_placeOrderWithAuthorizedDealer() {
            // Given
            LocalDate delivery = LocalDate.of(2026, 3, 25);

            // When
            Order order = system.placeOrder("Alice", "Lion", "FeedCo", 250.0, delivery);

            // Then
            assertNotNull(order);
            assertEquals("FeedCo", order.getDealerName());
            assertEquals(250.0, order.getInvoiceTotal());
            assertEquals(delivery, order.getExpectedDelivery());
            assertFalse(order.isArrived());

            Budget budget = system.getBudget("Lion");
            assertEquals(250.0, budget.getReserved());
            assertEquals(750.0, budget.getRemaining());
        }

        @Test
        @DisplayName("AC2: Given a zookeeper tries to order from an unauthorized dealer, " +
                "When they attempt to place the order, " +
                "Then the system rejects the order")
        void ac2_rejectUnauthorizedDealer() {
            // Given
            String unauthorizedDealer = "ShadyFeed Inc";

            // When / Then
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class,
                    () -> system.placeOrder("Alice", "Lion", unauthorizedDealer,
                            100.0, LocalDate.of(2026, 3, 20)));
            assertTrue(ex.getMessage().contains("not on the authorized"));
        }

        @Test
        @DisplayName("AC3: Given the order total would exceed the remaining budget, " +
                "When the zookeeper checks the order, " +
                "Then the system warns that the budget would be exceeded")
        void ac3_warnIfBudgetExceeded() {
            // Given
            system.placeOrder("Alice", "Lion", "FeedCo", 800.0,
                    LocalDate.of(2026, 3, 20));
            Budget budget = system.getBudget("Lion");

            // When
            boolean wouldExceed = budget.wouldExceedBudget(300.0);

            // Then
            assertTrue(wouldExceed,
                    "System should warn that 300 exceeds remaining budget of 200");
        }
    }

    // ==================================================================================
    // USER STORY 3: Handle Budget Increase Request
    //
    // Title: Request and process additional funds
    // Priority: Medium
    // Estimate: 5 story points
    //
    // As a zoo director,
    // I want to review and respond to budget increase requests from zookeepers,
    // so that I can ensure animals are properly fed while maintaining financial control.
    // ==================================================================================
    @Nested
    @DisplayName("US3: Request and process additional funds")
    class UserStory3_BudgetIncreaseRequest {

        @Test
        @DisplayName("AC1: Given a zookeeper has submitted a budget increase request, " +
                "When the zoo director views their messages, " +
                "Then the request with statement and link to budget is shown")
        void ac1_requestIsVisibleToDirector() {
            // Given
            BudgetRequest request = system.requestBudgetIncrease(
                    "Alice", "Lion",
                    "Lion needs special diet supplement", 500.0);

            // When
            List<String> messages = system.getMessages();
            Budget budget = system.getBudget("Lion");

            // Then
            assertEquals(BudgetRequest.Status.PENDING, request.getStatus());
            assertFalse(messages.isEmpty());
            assertTrue(messages.stream().anyMatch(m -> m.contains("Alice") && m.contains("Lion")));
            assertTrue(budget.getRequests().contains(request));
        }

        @Test
        @DisplayName("AC2: Given the zoo director grants a budget increase, " +
                "When they enter the increase amount and confirm, " +
                "Then the budget is increased and all responsible zookeepers are notified")
        void ac2_grantRequestIncreasesbudgetAndNotifies() {
            // Given
            BudgetRequest request = system.requestBudgetIncrease(
                    "Alice", "Elephant",
                    "Elephant needs extra hay for winter", 500.0);
            double budgetBefore = system.getBudget("Elephant").getTotalBudget();

            // When
            system.grantRequest(request, 500.0);

            // Then
            assertEquals(BudgetRequest.Status.GRANTED, request.getStatus());
            assertEquals(500.0, request.getGrantedAmount());
            assertEquals(budgetBefore + 500.0, system.getBudget("Elephant").getTotalBudget());

            List<String> messages = system.getMessages();
            // Both Alice and Bob are assigned to Elephant — both should be notified
            assertTrue(messages.stream().anyMatch(m ->
                    m.contains("Alice") && m.contains("granted")));
            assertTrue(messages.stream().anyMatch(m ->
                    m.contains("Bob") && m.contains("granted")));
        }

        @Test
        @DisplayName("AC3: Given the zoo director denies a budget increase, " +
                "When they write a denial statement, " +
                "Then the applicant is notified and budget overview shows denial remark")
        void ac3_denyRequestNotifiesApplicant() {
            // Given
            BudgetRequest request = system.requestBudgetIncrease(
                    "Alice", "Lion",
                    "Need premium feed", 300.0);
            double budgetBefore = system.getBudget("Lion").getTotalBudget();

            // When
            system.denyRequest(request, "Budget is tight this quarter");

            // Then
            assertEquals(BudgetRequest.Status.DENIED, request.getStatus());
            assertEquals("Budget is tight this quarter", request.getResponseStatement());
            assertEquals(budgetBefore, system.getBudget("Lion").getTotalBudget(),
                    "Budget should not change on denial");

            List<String> messages = system.getMessages();
            assertTrue(messages.stream().anyMatch(m ->
                    m.contains("Alice") && m.contains("denied")));
        }
    }

    // ==================================================================================
    // Additional tests: delivery confirmation, overdue orders, feed stock, expiration
    // ==================================================================================
    @Nested
    @DisplayName("Additional: Delivery, stock, and expiration")
    class AdditionalTests {

        @Test
        @DisplayName("When an order arrives, the invoice total is deducted from budget " +
                "and feed is added to stock")
        void deliveryConfirmationUpdatesStockAndBudget() {
            // Given
            Order order = system.placeOrder("Alice", "Lion", "FeedCo", 200.0,
                    LocalDate.of(2026, 3, 20));

            // When
            system.confirmDelivery(order, LocalDate.of(2026, 3, 19),
                    "Beef", 50.0, LocalDate.of(2026, 4, 19));

            // Then
            assertTrue(order.isArrived());
            assertEquals(200.0, system.getBudget("Lion").getSpent());
            assertEquals(0.0, system.getBudget("Lion").getReserved());

            List<FeedStock> stock = system.getStockForAnimal("Lion");
            assertEquals(1, stock.size());
            assertEquals("Beef", stock.get(0).getFeedName());
            assertEquals(50.0, stock.get(0).getQuantity());
        }

        @Test
        @DisplayName("An order past its expected delivery date is marked overdue")
        void overdueOrderIsHighlighted() {
            // Given
            Order order = system.placeOrder("Alice", "Lion", "FeedCo", 150.0,
                    LocalDate.of(2026, 3, 10));

            // When
            boolean overdue = order.isOverdue(LocalDate.of(2026, 3, 15));

            // Then
            assertTrue(overdue);
        }

        @Test
        @DisplayName("Feed past its expiration date is highlighted")
        void expiredFeedIsHighlighted() {
            // Given
            Order order = system.placeOrder("Alice", "Lion", "FeedCo", 100.0,
                    LocalDate.of(2026, 3, 10));
            system.confirmDelivery(order, LocalDate.of(2026, 3, 10),
                    "Fish", 20.0, LocalDate.of(2026, 3, 20));

            // When
            List<FeedStock> expired = system.getExpiredStock("Lion",
                    LocalDate.of(2026, 3, 25));

            // Then
            assertEquals(1, expired.size());
            assertEquals("Fish", expired.get(0).getFeedName());
        }

        @Test
        @DisplayName("Dealer can be removed from authorized list")
        void removeDealerFromWhitelist() {
            // Given
            assertTrue(system.isDealerAuthorized("FeedCo"));

            // When
            system.removeAuthorizedDealer("FeedCo");

            // Then
            assertFalse(system.isDealerAuthorized("FeedCo"));
            assertThrows(IllegalArgumentException.class,
                    () -> system.placeOrder("Alice", "Lion", "FeedCo", 100.0,
                            LocalDate.of(2026, 3, 20)));
        }
    }
}
