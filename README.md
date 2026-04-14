# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/img/logo-fiap.jpg" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
  </a>
</p>

## 👨‍🎓 Integrantes do Grupo

- Amanda Vieira Pires (RM566330)
- Ana Gabriela Soares Santos (RM565235)
- Bianca Nascimento de Santa Cruz Oliveira (RM561390)
- Milena Pereira dos Santos Silva (RM565464)
- Nayana Mehta Miazaki (RM565045)

## 👩‍🏫 Professores

### Tutor(a)

- Caique Nonato da Silva Bezerra

### Coordenador(a)

- André Godoi

---

# ❤️ CardioIA – Fase 2

## 🎯 Visão geral



## 📋 Objetivos e entregas


---

## 📊 Parte 1

## 📄 Parte 2 - Classificador básico de texto

Esta parte consiste em desenvolver uma ferramenta de análise preditiva para automação da triagem de saúde digital, classificando casos de alto e baixo risco. 

### 🚀 Objetivo

O objetivo é desenvolver uma solução de triagem digital para automação do suporte à decisão clínica, garantindo agilizade no atendimento, principalmente de casos críticos, utilizando algoritmos de processamento de linguagem natural (NLP) e modelo preiditivo de árvore de decisão.

### 📊 Estrutura dos Dados

A partir do arquivo `symtoms.txt` realizado na Parte 1, criamos o arquivo `triagem_risco.csv` que contém:
* **sintomas:** relato textual do paciente;
* **classificação:** risco classificado em alto e baixo;

### 🛠️ Tecnologias e Metodologia

#### **🧹 Limpeza dos dados**

* Remoção de valores ausentes (NaN) eliminando linhas vazias e incompletas que podem causar erros na execução do algoritmo;

* Normalização de texto convertendo todas as letras para minúsculas e remover espaços em branco desnecessários no começo e fim das frases, evitando que o modelo trate palavras idênticas como termos diferentes;

* Tratamento de caracteres especiais padronizando a codificação e garantindo a leitura correta de acentos e símbolos da língua portuguesa.

#### **🔢 Pré processamento de dados (NLP)**

O TF-IDF (*Term Frequency-Inverse Document Frequency*) foi aplicado para converter os relatos textuais dos pacientes em representações númericas. Esse processo permite que o modelo de Machine Learning compreenda e processe as palavras e calcule a importância de cada sintoma para realizar a classificação em baixo e alto risco.

#### **🌳 Modelo Preditivo**

O modelo **Árvore de Decisão** (*Decision Tree*) foi utilizado como uma estratégia pois ele funciona em uma lógica de "fluxograma", permitindo total transparência no diagnóstico.

**Divisão dos dados em teste e treino:**

* Treino (70%) para o algoritmos aprender os padrões e compreender as palavras-chave e níveis de risco;

* Teste (30%) para o modelo validar se realmente aprendeu ou apenas decorou as frases.

* A utilização da estratificação (`stratify=y`) garante que a proporção da classificação de "alto risco" e "baixo risco" seja igual no treino e no teste, evitando vieses.

A fim de decidir qual sintoma é mais importante, o modelo preditivo utiliza cálculos matemáticos de **Pureza**:

* **Gini (Índice de Impureza)**: mede a probabilidade de uma classificação incorreta para minimização de erros. Ele cria "nós" onde todos os exemplos dentro do mesmo nó pertencem à mesma classificação, ou seja, de "alto risco" ou de "baixo risco".

* **Entropia (Ganho de Informação)**: avalia a desordem dos dados ao selecionar palavras-chave que mais reduzem a incerteza sobre se o paciente é de alto ou baixo risco.

![Modelo Árvore de Decisão](assets/img/arvore_decisao.png)

#### **📊 Análise do Modelo Preditivo**

A Matriz de Confusão permite visualizar o desempenho em cada classificação de alto ou baixo risco, separando em Verdadeiros Positivos (quando o modelo acerta) dos Falsos Negativos (quando o modelo erra).

A partir da Análise da Matriz de Confusão, pode-se afirmar que:

* O modelo acertou 6 casos de baixo risco;
* O modelo errou 2 casos que originalmente seriam de alto risco porém classificou como baixo risco;
* O modelo errou 1 caso classificando-o como alto risco porém seria de baixo risco.

![Matriz de Confusão](assets/img/matriz_confusao.png)

### **✅ Conclusão**

O modelo preditivo resultou em uma acurácia de 67%, demonstrando uma forte tendência a classificar os sintomas como "baixo risco", conforme observado na Matriz de Confusão. Essa performance é atribuída à ambiguidade no dataset reduzido, onde as palavras-chaves nos relatos dos pacientes acabaram confundindo o algoritmo, dificultando a convergência.

Na próxima etapa, planeja-se aumentar a base de dados com palavras-chaves mais específicas para sindomas graves principalmente, a fim de mitigar os Falsos Negativos e aumentar a acurácia do modelo preditivo.

### **⚙️ Como executar a Parte 2**

1. Verificar de que o arquivo `triagem_risco.csv` está na pasta /document;
2. Abrir o arquivo `Classificador_Risco.ipynb` e executar com o Jupyter Notebook;
3. A execução da etapa 2 irá resultar no modelo preditivo com os gráficos gerados automaticamente ao final.