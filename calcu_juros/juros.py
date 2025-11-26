from datetime import datetime, date

def calcular_juros(valor, data_vencimento, data_atual=None):
    if data_atual is None:
        data_atual = date.today()

    dias_atraso = (data_atual - data_vencimento).days

    if dias_atraso <= 0:
        return 0.0, dias_atraso

    juros = valor * 0.025 * dias_atraso
    return juros, dias_atraso


def ler_data(mensagem):
    entrada = input(mensagem + " (DD/MM/AAAA): ")
    return datetime.strptime(entrada, "%d/%m/%Y").date()


def main():
    valor = float(input("Digite o valor original (R$): ").replace(",", "."))

    data_vencimento = ler_data("Digite a data de vencimento")
    data_hoje = date.today()

    juros, dias = calcular_juros(valor, data_vencimento, data_hoje)
    total = valor + juros

    print("\n====== CÁLCULO DE JUROS ======")
    print(f"Data de hoje: {data_hoje.strftime('%d/%m/%Y')}")
    print(f"Data de vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
    print(f"Dias de atraso: {dias if dias > 0 else 0}")
    print(f"Juros (2,5% ao dia): R$ {juros:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")


if __name__ == "__main__":
    main()
