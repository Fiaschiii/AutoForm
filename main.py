from pathlib import Path

import pandas as pd
from playwright.sync_api import sync_playwright

# Automação para preenchimento de formulário Google Forms

URL_FORMULARIO = "https://forms.gle/76cLpDVoDLeUo5qs7"
ARQUIVO_CSV = Path(__file__).parent / "auxilio_code" / "funcionarios_brasil_150.csv"

# Colunas do CSV na mesma ordem das perguntas do formulário
COLUNAS = ["Nome", "Sobrenome", "Setor", "ID da Empresa", "Cargo"]


def preencher_formulario(page, dados):
    page.goto(URL_FORMULARIO)
    perguntas = page.locator('div[role="listitem"]')
    perguntas.first.wait_for()

    # Cada pergunta tem um único campo (input de resposta curta ou textarea de parágrafo)
    for indice, valor in enumerate(dados):
        perguntas.nth(indice).locator('input[type="text"], textarea').fill(valor)

    page.get_by_role("button", name="Enviar").click()
    # Aguarda a página de confirmação para garantir que a resposta foi registrada
    page.wait_for_url("**/formResponse**")


def main():
    # dtype=str evita que o ID vire float (ex.: "1001.0"); fillna evita enviar "nan"
    tabela = pd.read_csv(ARQUIVO_CSV, dtype=str, encoding="utf-8-sig").fillna("")

    print("Início do código...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        for linha in tabela.index:
            dados = [tabela.loc[linha, coluna].strip() for coluna in COLUNAS]
            preencher_formulario(page, dados)
            print(f"[{linha + 1}/{len(tabela)}] Enviado: {dados[0]} {dados[1]}")

        browser.close()
    print("Fim do código.")


if __name__ == "__main__":
    main()
