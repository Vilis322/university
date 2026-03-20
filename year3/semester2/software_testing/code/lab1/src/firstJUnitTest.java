import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class firstJUnitTest {
    @Test
    public void first() {
        String str = "Hello Kyrylo";
        assertEquals("Hello Kyrylo", str);
    }
}
