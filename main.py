from collections import deque

# Entrada do quantum
quantum = int(input("Digite o valor do quantum: "))

# Entrada dos processos
processos = {}
n = int(input("Digite a quantidade de processos: "))

for i in range(1, n + 1):
    nome = input(f"Nome do processo {i}: ")
    burst = int(input(f"Tempo de execução de {nome}: "))
    processos[nome] = burst

# Estruturas auxiliares
fila = deque(processos.items())
tempo_corrente = 0
tempo_inicio = {}
tempo_finalizacao = {}
tempo_executado = {p: 0 for p in processos}
execucao = []

print("\nIniciando execução com Quantum =", quantum)
while fila:
    processo, tempo_restante = fila.popleft()

    if processo not in tempo_inicio:
        tempo_inicio[processo] = tempo_corrente

    tempo_a_executar = min(quantum, tempo_restante)
    tempo_corrente += tempo_a_executar
    tempo_executado[processo] += tempo_a_executar

    if tempo_restante > quantum:
        tempo_restante -= quantum
        fila.append((processo, tempo_restante))
        execucao.append(f"T={tempo_corrente}: {processo} executou por {tempo_a_executar} (restam {tempo_restante})")
    else:
        tempo_finalizacao[processo] = tempo_corrente
        execucao.append(f"T={tempo_corrente}: {processo} executou por {tempo_a_executar} e terminou")

# Cálculo dos tempos
turnaround_time = {p: tempo_finalizacao[p] for p in processos}
waiting_time = {p: turnaround_time[p] - tempo_executado[p] for p in processos}

# Impressão
print("\n--- LOG DE EXECUÇÃO ---")
for linha in execucao:
    print(linha)

print("\n--- TEMPOS POR PROCESSO ---")
for p in processos:
    print(f"{p}:")
    print(f"  - Turnaround time: {turnaround_time[p]}")
    print(f"  - Tempo de CPU: {tempo_executado[p]}")
    print(f"  - Tempo de espera: {waiting_time[p]}")

print("\nTempo total até todos os processos finalizarem:", tempo_corrente)