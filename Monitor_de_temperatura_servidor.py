limite_seguranca = 80
sistema_ativo = True

temperatura = float(input("Informe a temperatura do servidor: "))

while sistema_ativo:
    if temperatura > limite_seguranca:
        print(f"PERIGO! Temperatura em {temperatura}°C. Ativando coolers...")
        temperatura -= 10 # Simulando resfriamento
    else:
        print(f"Temperatura estável: {temperatura}°C.")
        sistema_ativo = False # Encerra simulação
