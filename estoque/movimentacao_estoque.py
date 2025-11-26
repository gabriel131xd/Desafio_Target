import json

ARQUIVO_ESTOQUE = "estoque.json"


def carregar_estoque(caminho=ARQUIVO_ESTOQUE):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    estoque = {}
    for item in dados["estoque"]:
        codigo = item["codigoProduto"]
        estoque[codigo] = {
            "descricao": item["descricaoProduto"],
            "quantidade": item["estoque"]
        }
    return estoque


def salvar_estoque(estoque, caminho=ARQUIVO_ESTOQUE):
    dados = {
        "estoque": [
            {
                "codigoProduto": codigo,
                "descricaoProduto": info["descricao"],
                "estoque": info["quantidade"]
            }
            for codigo, info in estoque.items()
        ]
    }
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def produtos(estoque):
    print("\n===== PRODUTOS =====")
    for codigo, info in estoque.items():
        print(f"{codigo} - {info['descricao']} (Estoque: {info['quantidade']})")


def listar_movimentacoes(movimentos):
    if not movimentos:
        print("\nNenhuma movimentação registrada ainda.")
        return

    print("\n=== RESUMO DAS MOVIMENTAÇÕES ===")
    for mov in movimentos:
        print(
            f"ID {mov['id']} | Produto {mov['produto']} | "
            f"{mov['tipo']} {mov['quantidade']} | {mov['descricao']} "
            f"| Estoque Final: {mov['estoqueFinal']}"
        )


def lancar_movimentacao(estoque, movimentos, proximo_id):
    produtos(estoque)

    codigo = int(input("\nDigite o código do produto (0 para cancelar): "))
    if codigo == 0:
        print("Movimentação cancelada.")
        return proximo_id

    if codigo not in estoque:
        print("Este código de produto não existe no estoque.")
        return proximo_id

    tipo = input("Tipo de movimentação (E = entrada, S = saída): ").upper()
    if tipo not in ("E", "S"):
        print("Tipo inválido!")
        return proximo_id

    quantidade = int(input("Quantidade: "))
    if quantidade <= 0:
        print("Quantidade inválida!")
        return proximo_id

    descricao_mov = input("Descrição da movimentação: ")

    if tipo == "S" and quantidade > estoque[codigo]["quantidade"]:
        print("Erro: estoque insuficiente!")
        return proximo_id

    if tipo == "E":
        estoque[codigo]["quantidade"] += quantidade
    else:
        estoque[codigo]["quantidade"] -= quantidade

    movimento = {
        "id": proximo_id,
        "produto": codigo,
        "descricao": descricao_mov,
        "tipo": "Entrada" if tipo == "E" else "Saída",
        "quantidade": quantidade,
        "estoqueFinal": estoque[codigo]["quantidade"]
    }

    movimentos.append(movimento)

    print("\nMovimentação registrada com sucesso!")
    print(f"ID: {movimento['id']}")
    print(f"Produto: {estoque[codigo]['descricao']}")
    print(f"Estoque final: {movimento['estoqueFinal']}")

    salvar_estoque(estoque)
    return proximo_id + 1


def main():
    estoque = carregar_estoque()
    movimentos = []
    proximo_id = 1

    while True:
        print("\n===== MENU ESTOQUE =====")
        print("1 - Lançar movimentação")
        print("2 - Listar produtos")
        print("3 - Listar movimentações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            proximo_id = lancar_movimentacao(estoque, movimentos, proximo_id)
        elif opcao == "2":
            produtos(estoque)
        elif opcao == "3":
            listar_movimentacoes(movimentos)
        else:
            print("Opção inválida!")

    print("\nSaindo... Estoque final salvo em arquivo.")


if __name__ == "__main__":
    main()
