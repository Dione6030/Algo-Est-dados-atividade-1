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

