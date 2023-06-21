# Validação de IPs
def validar_ip(ip):
    ip_split = ip.split('.')
    if len(ip_split) != 4:
        return False
    for octeto in ip_split:
        if not octeto.isdigit() or not (0 <= int(octeto) <= 255):
            return False
    return True


def calcular_ips_rede(ip, qtd_hosts):
    ip_split = ip.split('.')
    ip_decimal = int(ip_split[0]) << 24 | int(ip_split[1]) << 16 | int(ip_split[2]) << 8 | int(ip_split[3])

    # Cálculo da quantidade de bits para a submáscara
    submascara_bits = 32 - (qtd_hosts + 2).bit_length()

    # Cálculo do valor da submáscara
    submascara_decimal = (2 ** 32 - 1) - (2 ** (32 - submascara_bits) - 1)

    # Cálculo do endereço de rede
    ip_rede = ip_decimal & submascara_decimal

    # Cálculo do endereço de broadcast
    ip_broadcast = ip_rede | (2 ** (32 - submascara_bits) - 1)

    # Cálculo do primeiro e último IP disponível para os hosts
    ip_inicial = ip_rede + 1
    ip_final = ip_broadcast - 1

    ip_rede_str = '.'.join([str((ip_rede >> 24) & 0xFF),
                            str((ip_rede >> 16) & 0xFF),
                            str((ip_rede >> 8) & 0xFF),
                            str(ip_rede & 0xFF)])
    ip_broadcast_str = '.'.join([str((ip_broadcast >> 24) & 0xFF),
                                 str((ip_broadcast >> 16) & 0xFF),
                                 str((ip_broadcast >> 8) & 0xFF),
                                 str(ip_broadcast & 0xFF)])
    ip_inicial_str = '.'.join([str((ip_inicial >> 24) & 0xFF),
                               str((ip_inicial >> 16) & 0xFF),
                               str((ip_inicial >> 8) & 0xFF),
                               str(ip_inicial & 0xFF)])
    ip_final_str = '.'.join([str((ip_final >> 24) & 0xFF),
                             str((ip_final >> 16) & 0xFF),
                             str((ip_final >> 8) & 0xFF),
                             str(ip_final & 0xFF)])

    # Cálculo da submáscara de rede
    submascara_str = '.'.join([str((submascara_decimal >> 24) & 0xFF),
                               str((submascara_decimal >> 16) & 0xFF),
                               str((submascara_decimal >> 8) & 0xFF),
                               str(submascara_decimal & 0xFF)])

    return ip_rede_str, ip_broadcast_str, ip_inicial_str, ip_final_str, submascara_str


# Entrada dos dados pelo usuário
ip = input("Digite o endereço IP: ")
 
# Validação do IP
if not validar_ip(ip):
    print("Endereço IP inválido.")
else:
    qtd_hosts = int(input("Digite a quantidade de hosts desejada: "))
    # Cálculo dos IPs e da submáscara
    ip_rede, ip_broadcast, ip_inicial, ip_final, submascara = calcular_ips_rede(ip, qtd_hosts)

    # Impressão dos resultados
    print("IP de Rede:", ip_rede)
    print("IP de Broadcast:", ip_broadcast)
    print("IP Inicial:", ip_inicial)
    print("IP Final:", ip_final)
    print("Submáscara:", submascara)