public class Triangle {

    public static final int MIN = 1;
    public static final int MAX = 200;

    /**
     * Classifies a triangle given three side lengths.
     *
     * @param a first side
     * @param b second side
     * @param c third side
     * @return triangle type or an error message
     */
    public String classify(int a, int b, int c) {
        // c1: 1 <= a <= 200
        if (a < MIN || a > MAX) {
            return "Value of a is not in the range of permitted values.";
        }
        // c2: 1 <= b <= 200
        if (b < MIN || b > MAX) {
            return "Value of b is not in the range of permitted values.";
        }
        // c3: 1 <= c <= 200
        if (c < MIN || c > MAX) {
            return "Value of c is not in the range of permitted values.";
        }

        // c4: a + b > c
        // c5: a + c > b
        // c6: b + c > a
        if (a + b <= c || a + c <= b || b + c <= a) {
            return "NotATriangle";
        }

        if (a == b && b == c) {
            return "Equilateral";
        }

        if (a == b || b == c || a == c) {
            return "Isosceles";
        }

        return "Scalene";
    }
}
