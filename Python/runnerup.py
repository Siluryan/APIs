# Retorna o segundo maior valor numa lista

if __name__ == '__main__':
    m = []
    max_value = None


    def inserir_nota():
        c = 0
        t = 0

        t = int(input("insira o total de notas: "))
        n = int(input("insira a nota: "))
        m.append(str(n))

        c += 1

        while c < t:
            n = int(input("insira a nota: "))
            m.append(str(n))
            c += 1

    inserir_nota()

    max_value = None

    for x in m:
        if max_value is None or x > max_value:
            max_value = x

    m.remove(max_value)

    print(max(int(x) for x in m))
