#  Simulação de Incêndios Florestais (Forest Fire) — Trabalho Final de Sistemas Distribuídos

Este projeto implementa o *modelo de propagação de incêndios florestais (Forest Fire)* nas versões *sequencial, **paralela (com threads)* e *distribuída (com sockets TCP), conforme os requisitos da disciplina de **Sistemas Distribuídos*.

---

##  Objetivos do Projeto

- Implementar uma solução *sequencial, **paralela* e *distribuída* para o problema de simulação de incêndios.
- Comparar os *tempos de execução* entre as três abordagens.
- Discutir *escalabilidade, eficiência, limitações e melhorias*.
- Aplicar conceitos de *paralelismo* e *comunicação entre processos* em Python.

---

##  Tecnologias Utilizadas

- *Linguagem:* Python 3.11  
- *Bibliotecas:* numpy, matplotlib, threading, socket, pickle, time
- *IDE:* Visual Studio Code  
- *Sistema Operacional:* Windows 10 64 bits  

---

##  Estrutura do Projeto
bash
TrabalhoFinal_SistemasDistribuidos/
│
├── forestfire_sequencial.py
├── forestfire_paralelo.py
├── forestfire_distribuido/
│ ├── servidor.py
│ └── cliente.py
├── comparacao_resultados.py
├── tempoSimulacao.txt
├── grafico_tempos.png
└── README.md


---

##  Como Executar o Projeto

### 1️⃣ Instalar dependências
No terminal:
bash
pip install numpy matplotlib


### 2️⃣ Executar a versão sequencial
bash
python forestfire_sequencial.py


### 3️⃣ Executar a versão paralela
bash
python forestfire_paralelo.py


### 4️⃣ Executar a versão distribuída
Em dois terminais:
#### Servidor:
bash
cd forestfire_distribuido
python servidor.py


#### Cliente:
bash
cd forestfire_distribuido
python cliente.py


### 5️⃣ Gerar o gráfico comparativo
bash
python comparacao_resultados.py


---

## 📊 Resultados 

Os tempos de execução são armazenados no arquivo tempoSimulacao.txt, e o gráfico abaixo é gerado automaticamente:

## Análise Resumida

| Versão | Características | Desempenho | Observações |
|--------|----------------|-------------|--------------|
| *Sequencial* | Simples, executa célula por célula | Crescimento quadrático | Boa para pequenos N |
| *Paralela* | Divide linhas entre threads | Melhora com florestas grandes | Overhead de sincronização |
| *Distribuída* | Usa cliente/servidor via TCP | Boa escalabilidade | Latência e custo de rede impactam o tempo |

*Conclusão:*  
- Para problemas pequenos, a versão sequencial é mais eficiente.  
- Para tamanhos médios, a paralela oferece ganhos notáveis.  
- Para simulações grandes, a distribuída mostra melhor escalabilidade.

---

##  Limitações e Melhorias

*Limitações:*
- Sobrecarga na criação e sincronização de threads, o que reduz a eficiência em florestas pequenas.  
- Custo de serialização e envio de dados na versão distribuída, especialmente em matrizes grandes.  
- Dependência direta do hardware — quantidade de núcleos da CPU, velocidade de rede e memória disponível.  
- Sincronização global entre threads e processos pode causar espera desnecessária.  

*Melhorias sugeridas:*
- Utilizar multiprocessing para melhor aproveitamento de múltiplos núcleos, evitando limitações do GIL do Python.  
- Enviar apenas blocos modificados da floresta na comunicação via socket, reduzindo tráfego e tempo de rede.  
- Implementar versões com GPU (usando Numba ou CUDA) para acelerar o processamento em larga escala.  
- Testar o sistema em múltiplos hosts reais (não apenas localhost) para avaliar escalabilidade real.  
- Adotar compressão de dados (ex.: zlib) para otimizar o envio e recebimento de grandes matrizes.

---

##  Licença

Este projeto é de uso acadêmico e pode ser reutilizado para fins educacionais.
