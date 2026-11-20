# 🤖 Auto Form: cadastro automático de funcionários no Google Forms

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-automação_web-2EAD33?logo=playwright&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-dados-150458?logo=pandas&logoColor=white)

Automação em Python que lê uma planilha de funcionários e **preenche e envia um Google Forms para cada registro**, sem nenhuma digitação manual.

Na demonstração, **150 cadastros** são enviados em sequência a partir de um único arquivo CSV.

---

## 💡 O problema

Cadastrar funcionários um a um em um formulário é repetitivo, lento e sujeito a erro de digitação. Quando os dados já estão em uma planilha, não faz sentido redigitá-los.

## ✅ A solução

Um script que:

1. Lê a base de funcionários (`.csv`) com **Pandas**
2. Abre o formulário no navegador com **Playwright**
3. Preenche cada campo com os dados da linha
4. Envia e **aguarda a confirmação do Google Forms** antes de seguir para o próximo registro
5. Mostra o progresso no terminal

```
Início do código...
[1/150] Enviado: Lucas Silva
[2/150] Enviado: Mariana Araújo
[3/150] Enviado: Pedro Azevedo
...
Fim do código.
```

---

## ⚙️ Destaques técnicos

- **Seletores resilientes.** Os campos são localizados pela posição da pergunta no formulário (`div[role="listitem"]`), não por XPaths absolutos, que quebram com qualquer mudança no layout. O script funciona com perguntas de resposta curta (`input`) ou de parágrafo (`textarea`).
- **Envio garantido.** Depois de clicar em *Enviar*, o script espera a página de confirmação (`formResponse`). Assim nenhuma resposta se perde.
- **Um único navegador.** O navegador abre uma vez e o formulário é recarregado a cada registro, o que deixa o processo muito mais rápido do que abrir uma instância por linha.
- **Esperas automáticas.** Usa a espera embutida do Playwright no lugar de `time.sleep` fixos, então fica mais rápido e mais estável.
- **Dados tratados.** O CSV é lido como texto: IDs não viram `1001.0` e células vazias não são enviadas como `"nan"`.

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| **Python** | Linguagem principal |
| **Playwright** | Automação do navegador (Chromium) |
| **Pandas** | Leitura e tratamento da planilha |

---

## 📁 Estrutura do projeto

```
auto_form/
├── main.py                          # Script principal da automação
├── requirements.txt                 # Dependências
└── auxilio_code/
    ├── funcionarios_brasil_150.csv  # Base de exemplo com 150 funcionários
    └── tabela.py                    # Script auxiliar para visualizar a base
```

### Formato da planilha

```csv
Nome,Sobrenome,Setor,ID da Empresa,Cargo
Lucas,Silva,Marketing,1001,Social Media
Mariana,Araújo,Marketing,1002,Social Media
```

---

## 🚀 Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/Fiaschiii/auto_form.git
cd auto_form
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS
```

**3. Instale as dependências e o navegador do Playwright**
```bash
pip install -r requirements.txt
playwright install chromium
```

**4. Rode a automação**
```bash
python main.py
```

---

## 🔧 Adaptando para o seu formulário

No topo do `main.py`:

```python
URL_FORMULARIO = "https://forms.gle/..."          # link do seu formulário
ARQUIVO_CSV = ... / "funcionarios_brasil_150.csv" # sua planilha
COLUNAS = ["Nome", "Sobrenome", "Setor", "ID da Empresa", "Cargo"]
```

> ⚠️ A lista `COLUNAS` precisa seguir **a mesma ordem das perguntas do formulário**.

---

## 👨‍💻 Autor

**Miguel Fiaschi**

Curte automação e quer otimizar processos na sua empresa? Vamos conversar!

🌐 [miguelfiaschi.netlify.app](https://miguelfiaschi.netlify.app/)
