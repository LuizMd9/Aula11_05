while True:
    temperatura = float(input("Digite a temperatura do servidor: "))

    if temperatura > 80:
        print("ALERTA: Resfriamento ativado")
    else:
        print("Temperatura normal")

    comando = input("Deseja desligar o sistema? (sim/nao): ")

    if comando.lower() == "sim":
        print("Sistema desligado.")
        break