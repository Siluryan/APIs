import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Sort1 {
    private static final Strings suits[] = {"Hearts","Diamonds","Clubs","Spades"};

    // exibe elementos do array
    public void printElements(){
        List<String> list = Arrays.asList(suits);
        System.out.printf("Unsorted array elements:\n%s\n", list);
        Collections.sort(list); // classifica ArrayList

    //gera saída da lista
    System.out.printf("Sorted array elements:\n%s\n", list);
    }

    public static void main(String[] args) {
        Sort1 sort1 = new Sort1();
        sort1.printElements();
    }
}