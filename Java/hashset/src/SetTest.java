import java.util.*;

public class SetTest {
    private static final String colors[] = {
            "vermelho",
            "branco",
            "azul",
            "verde",
            "laranja",
            "branco",
            "cinza",
    };
    // cria um conjunto de array para eliminar duplicatas
    private void printNonDuplicates(Collection<String>collection)
    {
        //cria um HashSet
        Set<String> set = new HashSet<String>(collection);

        System.out.println("\nNonduplicates are");

        for (String s: set)
        System.out.printf("%s",s);

    }
    public SetTest(){
        List<String> list = Arrays.asList(colors);
        System.out.printf("ArrayList: %s\n", list);
        printNonDuplicates(list);
    }
}
