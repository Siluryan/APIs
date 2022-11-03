public class Main {

public static void main(String [] args) {
    
    Generic<T> g = new Generic<>(); // Substitua T pelo tipo desejado  

    g.add("Argumento do tipo especificado");

    System.out.println(g.getValue());    

    }

}