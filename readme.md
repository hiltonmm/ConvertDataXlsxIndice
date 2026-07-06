---

# 📖 Manual de Instalação e Uso: Conversor de Datas

Este sistema automatiza a conversão de datas em planilhas de Excel (`.xlsx`) para o formato **YYYY-mm-dd**.

---

### ⚠️ AVISO IMPORTANTE (LEIA ANTES DE USAR)

> **Nunca execute arquivos de Casamento e Óbito misturados na mesma pasta.** O script de Casamento procura por uma coluna específica, e o de Óbito procura por outra. **Execute sempre um tipo de índice por vez.** Após finalizar um lote, **retire os arquivos já processados da pasta** antes de iniciar o processamento do próximo lote (Óbito ou Casamento).

---

## 1. Instalação das Ferramentas (Apenas uma vez)

### A. Instalar o Python

1. Acesse [python.org/downloads](https://www.python.org/downloads/).
2. Clique no botão **"Download Python 3.x.x"**.
3. **MUITO IMPORTANTE:** Ao abrir o instalador, **marque a caixa "Add Python to PATH"** na parte inferior da tela.
4. Clique em **Install Now** e aguarde a conclusão.

### B. Instalar o Git

1. Acesse [git-scm.com](https://www.google.com/search?q=https://git-scm.com/downloads).
2. Clique em **Download for Windows**.
3. Execute o instalador e mantenha todas as configurações padrão (clique em "Next" até finalizar).

---

## 2. Como baixar o programa (Clonagem)

1. Escolha uma pasta onde deseja guardar o programa.
2. Clique com o botão direito dentro da pasta e selecione **"Open Git Bash here"** (ou abra o Terminal).
3. Digite o comando:
```bash
git clone https://github.com/hiltonmm/ConvertDataXlsxIndice.git

```


4. Entre na pasta criada.

---

## 3. Preparando o ambiente (Configuração Inicial)

*Apenas na primeira vez após baixar o programa:*

1. Encontre o arquivo **`setup_env.bat`**.
2. Dê um **duplo clique**. Uma janela preta vai abrir e instalar todas as ferramentas necessárias (`pandas` e `openpyxl`).
3. Quando ela terminar de rodar, pode fechar. O programa está pronto!

---

## 4. Como usar no dia a dia

**Passo 1: Organização**

* Coloque **apenas** os arquivos que você deseja converter na pasta.
* **Lembre-se:** Separe Casamento de Óbito em momentos diferentes.

**Passo 2: Execução**

* **Para planilhas de Casamento:** Dê um duplo clique no arquivo **`rodar_conversao_casamento.bat`**.
* **Para planilhas de Óbito:** Dê um duplo clique no arquivo **`rodar_conversao_obito.bat`**.

**Passo 3: Limpeza**

* Após a execução, você verá arquivos com o sufixo **`_Formatado.xlsx`**.
* **Importante:** Retire esses arquivos formatados da pasta antes de colocar o próximo lote, para manter seu ambiente organizado e evitar erros.

---

## 5. Perguntas Frequentes

* **"O programa não funcionou, o que houve?"**
Verifique se o nome da coluna de data no seu Excel está exatamente igual ao esperado pelo script. Se o erro for "Coluna não encontrada", abra o arquivo `.py` correspondente com o bloco de notas e verifique o nome exato da coluna.
* **"Como atualizo o meu programa?"**
Se você fizer melhorias no código e enviar para o GitHub, basta abrir o terminal na pasta e digitar: `git pull`.

---

*Dica: Se encontrar qualquer erro, tire um "print" da janela preta ou copie o texto de erro e envie para o suporte técnico.*