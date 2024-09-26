def inverter_string(s):
    # Inverte a string utilizando slicing
    return s[::-1]

# Entrada do usuário
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)

# Exibição do resultado
print(f"String invertida: {string_invertida}")