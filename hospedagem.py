def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # Crie o processamento das reservas:
    confirmadas = []
    recusadas = []
    
    # Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            # Se o quarto está disponível, a reserva é confirmada
            confirmadas.append(reserva)
            # O quarto agora fica indisponível para as próximas solicitações
            quartos_disponiveis.remove(reserva)
        else:
            # Se o quarto não está disponível, a reserva é recusada
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()
