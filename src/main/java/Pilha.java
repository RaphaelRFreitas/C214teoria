import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class Pilha<T> {
    private List<T> elementos = new ArrayList<T>();
    private int tamanho = 0;

    public int size() {
        return tamanho;
    }
    public boolean isEmpty() {
        return tamanho == 0;
    }
    public void push(T elemento) {
        elementos.add(elemento);
        tamanho++;
    }
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        T elemento = elementos.get(tamanho - 1);
        elementos.remove(tamanho - 1);
        tamanho--;
        return elemento;
    }
}
