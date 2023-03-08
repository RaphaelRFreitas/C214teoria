import org.junit.Test;

import java.util.EmptyStackException;

import static org.junit.Assert.*;

public class PilhaTeste {
    @Test
    public void testePilhaVazia() {
        Pilha<Integer> pilha = new Pilha<Integer>();
        assert pilha.isEmpty();
        assert pilha.size() == 0;
    }
    @Test
    public void testePush() {
        Pilha<Integer> pilha = new Pilha<Integer>();
        pilha.push(1);
        assert !pilha.isEmpty();
        assertFalse(pilha.isEmpty());
        assert pilha.size() == 1;
        pilha.push(2);
        assert !pilha.isEmpty();
        assert pilha.size() == 2;
    }
    @Test
    public void testePop() {
        Pilha<Integer> pilha = new Pilha<Integer>();
        pilha.push(1);
        assertFalse(pilha.isEmpty());
        pilha.push(2);
        assert pilha.pop() == 2;
        assert pilha.pop() == 1;
        assert pilha.isEmpty();
        assert pilha.size() == 0;
    }

    @Test (expected = EmptyStackException.class)
    public void testePopVazia() {
        Pilha<Integer> pilha = new Pilha<Integer>();
        pilha.pop();
    }

    @Test
    public void testePushPop() {
        Pilha<Integer> pilha = new Pilha<Integer>();
        pilha.push(1);
        pilha.push(2);
        assert pilha.pop() == 2;
        assert pilha.pop() == 1;
        assert pilha.isEmpty();
        assert pilha.size() == 0;
    }
}
