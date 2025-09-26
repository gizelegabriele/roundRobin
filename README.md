# Controle de Processos com Round Robin  

Este projeto implementa o algoritmo de escalonamento de processos *Round Robin* em Python, o objetivo é simular a execução de múltiplos processos com um *quantum fixo* de tempo.  

## 💻 Algoritmo Round Robin  

O **Round Robin** é um algoritmo de escalonamento preemptivo projetado para oferecer "justiça" na distribuição do tempo de CPU entre os processos.  

1. **Quantum:** O algoritmo utiliza um intervalo fixo de tempo, chamado **quantum**.  
2. **Execução:** Cada processo na fila de prontos é executado por, no máximo, o tempo do quantum.  
3. **Preempção:**  
   - Se o processo não terminar dentro do quantum, ele é **interrompido (preemptado)** e movido para o **fim da fila** para aguardar sua próxima rodada.  
   - Se o processo terminar antes do quantum, ele é finalizado e o escalonador passa imediatamente para o próximo processo na fila.  

O programa simula a execução em ciclos, mostrando qual processo está em execução a cada quantum.  

---
### Cenário de Simulação

O programa deve ser testado com o seguinte cenário:  

| Processo   | Tempo Total Necessário               |
|------------|--------------------------------------|
| Processo 1 | 10 unidades de tempo                 |
| Processo 2 | 5 unidades de tempo                  |
| Processo 3 | 8 unidades de tempo                  |  

**Quantum Definido:** **2 unidades de tempo**.  

---

### Como Executar o Programa  

#### Pré-requisitos:

Você precisa ter o **Python** instalado na máquina.  

#### Configuração Inicial - Clonando o Repositório:

1.  Abra o terminal 
2.  Clone o repositório do GitHub:

```bash
git clone https://github.com/gizelegabriele/roundRobin.git
```
3. Abra o projeto na IDE.
4. No terminal, digite o comando abaixo para executar o programa:
```bash
python main.py
```  
--- 
###  Considerações:

Projeto desenvolvido na competência de *Desenvolver simulador de abstrações de recursos de S.O* orientado pela professora Anna Beatriz Lucena.

#### Integrantes:

- Diogo Fernando — 2313080079  
- Fábio Dantas Filho — 2313080081  
- Gizele Gabriele Vidal de Sousa — 2313080143  
- Gustavo de Sousa Maciel — 2313080131  
- Renata Cardoso Mantovani — 2313080105  
