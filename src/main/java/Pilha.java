import java.util.ArrayList;
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
}
