## Interfaces e Classes

Uma **interface** dá um nome para um conjunto de constantes e operações (assinaturas de métodos). Estas constantes e operações modelam um certo comportamento. O interesse nas inteerfaces ocorre pelo fato de podermos definir **o que** é feito sem termos que definir como (não existem instâncias de interfaces).

Uma **classe** dá um nome para um conjunto de campos e métodos(funções e procedimentos). Estes campos e métodos modelam um certo conceito. O interesse nas classes ocorre,basicamente em duas situações. Primeiramente, pelo fato de que um comando só pode existir dentro de um elemento(p.ex. um método) de uma classe. Em segundo lugar, pelo fato de que uma classe define um tipo. Podemos assim definir variáveis que irão conter referências para instâncias da respectiva classe.

## List e ArrayList

List e ArrayList são os membros do framework Collection.

**List** é uma coleção de elementos em uma sequência em que cada elemento é um objeto e os elementos são acessados por sua posição (index).

**ArrayList** cria uma matriz dinâmica de objetos que aumenta ou reduz de tamanho sempre que necessário.

A principal diferença entre List e ArrayList é que **List** é uma interface e **ArrayList** é uma classe.


## Diferença entre as interfaces List, Set e Map

### 1. Ordenação

**List** representa uma sequência ordenada cujos elementos são accessíves por índice.

**Set** representa uma coleção DISTINTA de elementos que podem ser ordenados ou não, dependendo da implementação. 
    Ex:
    **HashSet** é desordenada;
    **LinkedHashSet** é ordenada;
    **TreeSet** é ordenada por ordem natural ou por algum comparador fornecido.

**Map** representa o mapeamento da chave para valores. A ordenação em Map também é específica para cada implementação.
    Ex:
    **TreeMap** é ordenada;
    **HashMap** não é ordenada.

### 2. Duplicatas

Em **List** podemos ter elementos duplicados. **Set** contém apenas elementos distintos e em **Map** não é permitido chaves duplicadas.

### 3. Valores Nulos

**List** permite qualquer número de valores nulos, enquanto **Set** contém no máximo um elemento nulo. **Map** normalmente permite null como chave e valor, mas algumas implementações proíbem chaves e valores nulos.

4. Casos de Uso

**List**: quando se quer manes a ordem dos elementos;
**Set**: impedir a inserção de elementos duplicados;
**Map**: recuperação rápida de dados do tipo chave-valor.

Ref:

https://www.alura.com.br/conteudo/java-collections--amp?gclid=Cj0KCQiAgribBhDkARIsAASA5bu4N7r1Ujq-ralR60PjEOKSKUfVZqE4c-T_ihTGLZl6sB93mz7eAvEaAhraEALw_wcB

https://homepages.dcc.ufmg.br/~rodolfo/aedsi-2-09/

https://www.techiedelight.com/pt/difference-between-list-set-map-interface-java/