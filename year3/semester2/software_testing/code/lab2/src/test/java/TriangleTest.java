import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class TriangleTest {

    private Triangle triangle;

    @BeforeEach
    void setUp() {
        triangle = new Triangle();
    }

    // ==================================================================================
    // 1. BOUNDARY VALUE ANALYSIS (BVA)
    //    For each variable a, b, c in [1, 200], test at: min, min+1, nominal, max-1, max
    //    Hold other variables at nominal value (100).
    // ==================================================================================
    @Nested
    @DisplayName("Boundary Value Analysis")
    class BoundaryValueAnalysis {

        // --- Variable a boundaries (b=100, c=100) ---
        @Test
        @DisplayName("BVA: a=1, b=100, c=100 -> Isosceles")
        void bva_a_min() {
            assertEquals("Isosceles", triangle.classify(1, 100, 100));
        }

        @Test
        @DisplayName("BVA: a=2, b=100, c=100 -> Isosceles")
        void bva_a_minPlus1() {
            assertEquals("Isosceles", triangle.classify(2, 100, 100));
        }

        @Test
        @DisplayName("BVA: a=100, b=100, c=100 -> Equilateral")
        void bva_a_nominal() {
            assertEquals("Equilateral", triangle.classify(100, 100, 100));
        }

        @Test
        @DisplayName("BVA: a=199, b=100, c=100 -> Isosceles")
        void bva_a_maxMinus1() {
            assertEquals("Isosceles", triangle.classify(199, 100, 100));
        }

        @Test
        @DisplayName("BVA: a=200, b=100, c=100 -> NotATriangle")
        void bva_a_max() {
            assertEquals("NotATriangle", triangle.classify(200, 100, 100));
        }

        // --- Variable b boundaries (a=100, c=100) ---
        @Test
        @DisplayName("BVA: a=100, b=1, c=100 -> Isosceles")
        void bva_b_min() {
            assertEquals("Isosceles", triangle.classify(100, 1, 100));
        }

        @Test
        @DisplayName("BVA: a=100, b=2, c=100 -> Isosceles")
        void bva_b_minPlus1() {
            assertEquals("Isosceles", triangle.classify(100, 2, 100));
        }

        @Test
        @DisplayName("BVA: a=100, b=199, c=100 -> Isosceles")
        void bva_b_maxMinus1() {
            assertEquals("Isosceles", triangle.classify(100, 199, 100));
        }

        @Test
        @DisplayName("BVA: a=100, b=200, c=100 -> NotATriangle")
        void bva_b_max() {
            assertEquals("NotATriangle", triangle.classify(100, 200, 100));
        }

        // --- Variable c boundaries (a=100, b=100) ---
        @Test
        @DisplayName("BVA: a=100, b=100, c=1 -> Isosceles")
        void bva_c_min() {
            assertEquals("Isosceles", triangle.classify(100, 100, 1));
        }

        @Test
        @DisplayName("BVA: a=100, b=100, c=2 -> Isosceles")
        void bva_c_minPlus1() {
            assertEquals("Isosceles", triangle.classify(100, 100, 2));
        }

        @Test
        @DisplayName("BVA: a=100, b=100, c=199 -> Isosceles")
        void bva_c_maxMinus1() {
            assertEquals("Isosceles", triangle.classify(100, 100, 199));
        }

        @Test
        @DisplayName("BVA: a=100, b=100, c=200 -> NotATriangle")
        void bva_c_max() {
            assertEquals("NotATriangle", triangle.classify(100, 100, 200));
        }
    }

    // ==================================================================================
    // 2. EQUIVALENCE PARTITIONING
    //    Partition the input space into equivalence classes and pick one representative
    //    from each class.
    // ==================================================================================
    @Nested
    @DisplayName("Equivalence Partitioning")
    class EquivalencePartitioning {

        // --- Valid equivalence classes ---
        @Test
        @DisplayName("EP: Equilateral triangle")
        void ep_equilateral() {
            assertEquals("Equilateral", triangle.classify(50, 50, 50));
        }

        @Test
        @DisplayName("EP: Isosceles triangle (a == b)")
        void ep_isosceles_ab() {
            assertEquals("Isosceles", triangle.classify(50, 50, 30));
        }

        @Test
        @DisplayName("EP: Isosceles triangle (b == c)")
        void ep_isosceles_bc() {
            assertEquals("Isosceles", triangle.classify(30, 50, 50));
        }

        @Test
        @DisplayName("EP: Isosceles triangle (a == c)")
        void ep_isosceles_ac() {
            assertEquals("Isosceles", triangle.classify(50, 30, 50));
        }

        @Test
        @DisplayName("EP: Scalene triangle")
        void ep_scalene() {
            assertEquals("Scalene", triangle.classify(30, 40, 50));
        }

        @Test
        @DisplayName("EP: Scalene triangle (different values)")
        void ep_scalene_2() {
            assertEquals("Scalene", triangle.classify(10, 15, 20));
        }

        // --- Invalid equivalence classes: range violations ---
        @Test
        @DisplayName("EP: a below range")
        void ep_a_belowRange() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(0, 50, 50));
        }

        @Test
        @DisplayName("EP: a above range")
        void ep_a_aboveRange() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(201, 50, 50));
        }

        @Test
        @DisplayName("EP: b below range")
        void ep_b_belowRange() {
            assertEquals("Value of b is not in the range of permitted values.",
                    triangle.classify(50, 0, 50));
        }

        @Test
        @DisplayName("EP: b above range")
        void ep_b_aboveRange() {
            assertEquals("Value of b is not in the range of permitted values.",
                    triangle.classify(50, 201, 50));
        }

        @Test
        @DisplayName("EP: c below range")
        void ep_c_belowRange() {
            assertEquals("Value of c is not in the range of permitted values.",
                    triangle.classify(50, 50, 0));
        }

        @Test
        @DisplayName("EP: c above range")
        void ep_c_aboveRange() {
            assertEquals("Value of c is not in the range of permitted values.",
                    triangle.classify(50, 50, 201));
        }

        // --- Invalid equivalence class: not a triangle ---
        @Test
        @DisplayName("EP: NotATriangle (a + b <= c)")
        void ep_notATriangle() {
            assertEquals("NotATriangle", triangle.classify(1, 2, 100));
        }
    }

    // ==================================================================================
    // 3. ERROR GUESSING
    //    Test edge cases and common mistakes that might reveal defects.
    // ==================================================================================
    @Nested
    @DisplayName("Error Guessing")
    class ErrorGuessing {

        @Test
        @DisplayName("EG: Negative value for a")
        void eg_negativeA() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(-1, 50, 50));
        }

        @Test
        @DisplayName("EG: Negative value for b")
        void eg_negativeB() {
            assertEquals("Value of b is not in the range of permitted values.",
                    triangle.classify(50, -5, 50));
        }

        @Test
        @DisplayName("EG: Negative value for c")
        void eg_negativeC() {
            assertEquals("Value of c is not in the range of permitted values.",
                    triangle.classify(50, 50, -10));
        }

        @Test
        @DisplayName("EG: All zeros")
        void eg_allZeros() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(0, 0, 0));
        }

        @Test
        @DisplayName("EG: All at maximum boundary")
        void eg_allMax() {
            assertEquals("Equilateral", triangle.classify(200, 200, 200));
        }

        @Test
        @DisplayName("EG: All at minimum boundary")
        void eg_allMin() {
            assertEquals("Equilateral", triangle.classify(1, 1, 1));
        }

        @Test
        @DisplayName("EG: Degenerate triangle a + b == c (not a triangle)")
        void eg_degenerateAB() {
            assertEquals("NotATriangle", triangle.classify(50, 50, 100));
        }

        @Test
        @DisplayName("EG: Degenerate triangle a + c == b (not a triangle)")
        void eg_degenerateAC() {
            assertEquals("NotATriangle", triangle.classify(50, 100, 50));
        }

        @Test
        @DisplayName("EG: Degenerate triangle b + c == a (not a triangle)")
        void eg_degenerateBC() {
            assertEquals("NotATriangle", triangle.classify(100, 50, 50));
        }

        @Test
        @DisplayName("EG: Just barely a valid triangle (a + b == c + 1)")
        void eg_barelyValid() {
            assertEquals("Isosceles", triangle.classify(50, 50, 99));
        }

        @Test
        @DisplayName("EG: Large difference between sides -> not a triangle")
        void eg_largeDifference() {
            assertEquals("NotATriangle", triangle.classify(1, 1, 200));
        }

        @Test
        @DisplayName("EG: Integer.MIN_VALUE")
        void eg_intMinValue() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(Integer.MIN_VALUE, 50, 50));
        }

        @Test
        @DisplayName("EG: Very large negative")
        void eg_veryLargeNegative() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(-1000, 50, 50));
        }
    }

    // ==================================================================================
    // 4. BRANCH / CONDITION COVERAGE
    //    Ensure every branch and condition in classify() is exercised.
    // ==================================================================================
    @Nested
    @DisplayName("Branch and Condition Coverage")
    class BranchConditionCoverage {

        // --- c1: a < MIN ---
        @Test
        @DisplayName("Branch: a < MIN")
        void branch_a_lessThanMin() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(0, 100, 100));
        }

        // --- c1: a > MAX ---
        @Test
        @DisplayName("Branch: a > MAX")
        void branch_a_greaterThanMax() {
            assertEquals("Value of a is not in the range of permitted values.",
                    triangle.classify(201, 100, 100));
        }

        // --- c2: b < MIN ---
        @Test
        @DisplayName("Branch: b < MIN")
        void branch_b_lessThanMin() {
            assertEquals("Value of b is not in the range of permitted values.",
                    triangle.classify(100, 0, 100));
        }

        // --- c2: b > MAX ---
        @Test
        @DisplayName("Branch: b > MAX")
        void branch_b_greaterThanMax() {
            assertEquals("Value of b is not in the range of permitted values.",
                    triangle.classify(100, 201, 100));
        }

        // --- c3: c < MIN ---
        @Test
        @DisplayName("Branch: c < MIN")
        void branch_c_lessThanMin() {
            assertEquals("Value of c is not in the range of permitted values.",
                    triangle.classify(100, 100, 0));
        }

        // --- c3: c > MAX ---
        @Test
        @DisplayName("Branch: c > MAX")
        void branch_c_greaterThanMax() {
            assertEquals("Value of c is not in the range of permitted values.",
                    triangle.classify(100, 100, 201));
        }

        // --- c4: a + b <= c ---
        @Test
        @DisplayName("Branch: a + b <= c")
        void branch_c4_notATriangle() {
            assertEquals("NotATriangle", triangle.classify(10, 20, 100));
        }

        // --- c5: a + c <= b ---
        @Test
        @DisplayName("Branch: a + c <= b")
        void branch_c5_notATriangle() {
            assertEquals("NotATriangle", triangle.classify(10, 100, 20));
        }

        // --- c6: b + c <= a ---
        @Test
        @DisplayName("Branch: b + c <= a")
        void branch_c6_notATriangle() {
            assertEquals("NotATriangle", triangle.classify(100, 10, 20));
        }

        // --- Equilateral branch ---
        @Test
        @DisplayName("Branch: Equilateral (a == b && b == c)")
        void branch_equilateral() {
            assertEquals("Equilateral", triangle.classify(75, 75, 75));
        }

        // --- Isosceles: a == b only ---
        @Test
        @DisplayName("Branch: Isosceles (a == b, b != c)")
        void branch_isosceles_ab() {
            assertEquals("Isosceles", triangle.classify(75, 75, 50));
        }

        // --- Isosceles: b == c only ---
        @Test
        @DisplayName("Branch: Isosceles (b == c, a != b)")
        void branch_isosceles_bc() {
            assertEquals("Isosceles", triangle.classify(50, 75, 75));
        }

        // --- Isosceles: a == c only ---
        @Test
        @DisplayName("Branch: Isosceles (a == c, a != b)")
        void branch_isosceles_ac() {
            assertEquals("Isosceles", triangle.classify(75, 50, 75));
        }

        // --- Scalene branch ---
        @Test
        @DisplayName("Branch: Scalene (all sides different)")
        void branch_scalene() {
            assertEquals("Scalene", triangle.classify(30, 40, 50));
        }
    }

    // ==================================================================================
    // 5. PARAMETERIZED TESTS
    //    Compact representation of multiple test vectors via @CsvSource.
    // ==================================================================================
    @Nested
    @DisplayName("Parameterized Tests")
    class ParameterizedTests {

        @ParameterizedTest(name = "Scalene({0}, {1}, {2})")
        @DisplayName("Various scalene triangles")
        @CsvSource({
                "3, 4, 5",
                "5, 7, 10",
                "10, 15, 20",
                "100, 150, 200",
                "7, 8, 9"
        })
        void scaleneTriangles(int a, int b, int c) {
            assertEquals("Scalene", triangle.classify(a, b, c));
        }

        @ParameterizedTest(name = "Equilateral({0}, {1}, {2})")
        @DisplayName("Various equilateral triangles")
        @CsvSource({
                "1, 1, 1",
                "50, 50, 50",
                "100, 100, 100",
                "200, 200, 200"
        })
        void equilateralTriangles(int a, int b, int c) {
            assertEquals("Equilateral", triangle.classify(a, b, c));
        }

        @ParameterizedTest(name = "NotATriangle({0}, {1}, {2})")
        @DisplayName("Various not-a-triangle cases")
        @CsvSource({
                "1, 1, 200",
                "1, 200, 1",
                "200, 1, 1",
                "50, 50, 100",
                "1, 2, 3"
        })
        void notATriangleCases(int a, int b, int c) {
            assertEquals("NotATriangle", triangle.classify(a, b, c));
        }

        @ParameterizedTest(name = "OutOfRange({0}, {1}, {2})")
        @DisplayName("Various out-of-range cases")
        @CsvSource({
                "0, 50, 50",
                "201, 50, 50",
                "-1, 50, 50",
                "50, 0, 50",
                "50, 201, 50",
                "50, 50, 0",
                "50, 50, 201"
        })
        void outOfRangeCases(int a, int b, int c) {
            String result = triangle.classify(a, b, c);
            assertTrue(result.contains("not in the range of permitted values"),
                    "Expected range error for (" + a + ", " + b + ", " + c + "), got: " + result);
        }
    }
}
