funcionalidades = {"Ler": True,
            "Escrever": True,
            "Apagar": True,
            "Exportar": True}

def geraCombinacoes(funcionalidades):
    quantidade = len(funcionalidades)
    if total <= 9:
        partes = dividirTrabalho(0, total, 2, quantidade)
    else:
        partes = dividirTrabalho(0, total, 4, quantidade)
    
    return partes

def dividirTrabalho(inicio, fim, divisao, quantidade):
    if fim - inicio <= divisao:
        apresentaCombinacoes(inicio, fim, quantidade)
        return
    
    meio = (inicio + fim) // 2
    
    dividirTrabalho(inicio, meio, divisao, quantidade)
    dividirTrabalho(meio, fim, divisao, quantidade)

def apresentaCombinacoes(inicio, fim, quantidade):
    for i in range(inicio, fim):
        combinacao = [0] * quantidade
        
        for j in range(quantidade):
            bit = (i >> j) & 1
            combinacao[quantidade - 1 - j] = bit
        
        print(combinacao)
