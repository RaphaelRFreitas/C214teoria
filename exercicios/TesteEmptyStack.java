import org.junit.Test;
import static org.junit.Assert.*;
import java.util.EmptyStackException;
public class TesteEmptyStack {
    @Test(expected = EmptyStackException.class)
    public void testEmptyStackException()
    {
        Stack s<Integer > = new Stack<Integer>();
        s.push(1);
        s.pop();
        s.pop();
    }
}