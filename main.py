from binarySearchTree import BinarySearchTree

from binarytree import build

searchBynaryTree = BinarySearchTree()

values = []


def carregar_arquivo():
    with open("entrada.txt", "r") as entries:
        data = entries.readlines()

        result = list(map(lambda x: x.strip().replace("\n", ""), data))

        for item in result:
            searchBynaryTree.insert(item)
            values.append(item)

    graph = build(values)

    print(graph)
    print("\n")

    print("\nOpção 1 selecionada - Carregar o arquivo de nomes na ABB")


def mostrar_arvore_4_niveis():
    searchBynaryTree.print_first_four_levels()
    print(
        "\nOpção 2 selecionada - Mostrar árvore (os 4 primeiros níveis): caminhamento por nível"
    )


def mostrar_arvore_todos_niveis():
    searchBynaryTree.level_order_traversal()
    print(
        "\nOpção 3 selecionada - Mostrar a árvore (todos os níveis): caminhamento por nível"
    )


def mostrar_arvore_pre_ordem():
    searchBynaryTree.preorder_traversal()
    print("\nOpção 4 selecionada - Mostrar a árvore: pré-ordem")


def mostrar_arvore_in_ordem():
    searchBynaryTree.inorder_traversal()
    print("\nOpção 5 selecionada - Mostrar a árvore: In-ordem")


def mostrar_arvore_pos_ordem():
    searchBynaryTree.postorder_traversal()
    print("\nOpção 6 selecionada - Mostrar a árvore: pós-ordem")


def remover_elemento():
    element_to_be_removed = input("Insira o elemento a ser removido: ")

    searchBynaryTree.remove(element_to_be_removed)

    values.pop(values.index(element_to_be_removed))

    graph = build(values)

    print(graph)
    print("\n")
    print("\nOpção 7 selecionada - Remover um elemento da árvore")


# Função principal do programa
def main():
    while True:
        print("\nMenu:")
        print("1- Carregar o arquivo de nomes na ABB")
        print("2- Mostrar árvore (os 4 primeiros níveis): caminhamento por nível")
        print("3- Mostrar a árvore (todos os níveis): caminhamento por nível")
        print("4- Mostrar a árvore: pré-ordem")
        print("5- Mostrar a árvore: In-ordem")
        print("6- Mostrar a árvore: pós-ordem")
        print("7- Remover um elemento da árvore")
        print("8- Encerrar")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            carregar_arquivo()
        elif opcao == "2":
            mostrar_arvore_4_niveis()
        elif opcao == "3":
            mostrar_arvore_todos_niveis()
        elif opcao == "4":
            mostrar_arvore_pre_ordem()
        elif opcao == "5":
            mostrar_arvore_in_ordem()
        elif opcao == "6":
            mostrar_arvore_pos_ordem()
        elif opcao == "7":
            remover_elemento()
        elif opcao == "8":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")


if __name__ == "__main__":
    main()
