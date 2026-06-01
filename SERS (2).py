# GLOBAL SOLUTION - MONITORAMENTO ESPACIAL
# Soluções em Energias Renováveis e Sustentáveis

import random
import time

# FUNÇÕES DE SIMULAÇÃO

def gerar_temperatura():
    return random.randint(-20, 120)

def gerar_energia():
    return random.randint(0, 100)

def gerar_comunicacao():
    return random.choice(["ONLINE", "INSTÁVEL", "OFFLINE"])

def gerar_status_modulo():
    return random.choice(["OPERANDO", "MANUTENÇÃO", "CRÍTICO"])

# FUNÇÃO DE ALERTAS

def verificar_alertas(temp, energia, comunicacao, status):
    alertas = []

    if temp > 90:
        alertas.append("ALERTA: Temperatura extremamente alta!")

    if temp < -10:
        alertas.append("ALERTA: Temperatura extremamente baixa!")

    if energia < 20:
        alertas.append("ALERTA: Nível de energia crítico!")

    if comunicacao == "OFFLINE":
        alertas.append("ALERTA: Falha total na comunicação!")

    if status == "CRÍTICO":
        alertas.append("ALERTA: Módulo em estado crítico!")

    return alertas

# TOMADA DE DECISÃO AUTOMÁTICA

def tomada_decisao(temp, energia, comunicacao, status):

    print("\n[AÇÕES AUTOMÁTICAS]")

    if temp > 90:
        print("- Ativando sistema de resfriamento.")

    if energia < 20:
        print("- Reduzindo consumo energético.")

    if comunicacao == "OFFLINE":
        print("- Tentando reconectar antena principal.")

    if status == "CRÍTICO":
        print("- Enviando equipe virtual de manutenção.")

    if (
        temp <= 90
        and energia >= 20
        and comunicacao != "OFFLINE"
        and status != "CRÍTICO"
    ):
        print("- Sistema operando normalmente.")

# EXIBIÇÃO DOS DADOS

def mostrar_dados(temp, energia, comunicacao, status):

    print(" MONITORAMENTO DA MISSÃO ESPACIAL ")

    print(f"Temperatura: {temp} °C")
    print(f"Energia: {energia}%")
    print(f"Comunicação: {comunicacao}")
    print(f"Status do módulo: {status}")

    alertas = verificar_alertas(temp, energia, comunicacao, status)

    print("\n[ALERTAS]")
    if alertas:
        for alerta in alertas:
            print(alerta)
    else:
        print("Nenhum alerta detectado.")

    tomada_decisao(temp, energia, comunicacao, status)

# LOOP PRINCIPAL

def iniciar_monitoramento():

    print("Iniciando sistema inteligente...\n")

    for i in range(5):

        temperatura = gerar_temperatura()
        energia = gerar_energia()
        comunicacao = gerar_comunicacao()
        status = gerar_status_modulo()

        mostrar_dados(
            temperatura,
            energia,
            comunicacao,
            status
        )

        time.sleep(2)

# EXECUÇÃO

iniciar_monitoramento()
