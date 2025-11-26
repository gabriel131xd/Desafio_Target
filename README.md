# Desafio Técnico – Python (Comissão, Estoque e Juros)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](#)
[![Status](https://img.shields.io/badge/status-concluído-success)](#)
[![Made with](https://img.shields.io/badge/made%20with-Python-orange)](https://www.python.org/)

Repositório contendo a implementação de três desafios técnicos em Python, envolvendo cálculo de comissão de vendas, movimentações de estoque e cálculo de juros por atraso.

---

## 🔹 Desafio 1 – Comissão por Vendedor

**Arquivo:** `comissao.py`  
**Entrada de dados:** `vendas.json`

Regra de comissão por venda:

- Vendas **abaixo de R$ 100,00** → não geram comissão  
- Vendas **abaixo de R$ 500,00** → 1% de comissão  
- Vendas **a partir de R$ 500,00** → 5% de comissão  

O programa:

1. Lê o arquivo `vendas.json`
2. Calcula a comissão de cada venda
3. Agrupa por vendedor
4. Exibe o total de comissão por vendedor no terminal

### Como rodar

```bash
python comissao.py
