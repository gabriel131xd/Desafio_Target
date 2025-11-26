import json

def carregar_vendas(caminho="vendas.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def calculo_comissao(valor):
    if valor < 100:
        return 0.0
    if valor < 500:
        return valor * 0.01
    return valor * 0.05

def main():
    dados = carregar_vendas()
    vendas = dados["vendas"]

    comissoes = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]
        valor_comissao = calculo_comissao(valor)

        if vendedor not in comissoes:
            comissoes[vendedor] = 0

        comissoes[vendedor] += valor_comissao

    print("\n===== Comissão por Vendedor =====")
    for vendedor, total in comissoes.items():
        print(f"{vendedor}: R$ {total:.2f}")

if __name__ == "__main__":
    main()
