import json

print("DIGITE O NUMERO DO CODIGO:\n")
entrada = input("MENU\nCódigo [1]\nCódigo[2]\nCódigo[3]\nCódigo[4]\nCódigo[5]\n")

if entrada == '1':
    INDICE = 13
    SOMA = 0
    K = 0
    
    while K < INDICE:  
        K = K + 1;
        SOMA = SOMA + K;
    
    print(SOMA);

if entrada == '2':

    def pertence_a_fibonacci(n):
        # Inicializa os dois primeiros números da sequência
        a, b = 0, 1
        
        # Verifica se o número informado é 0 ou 1, que são parte da sequência
        if n == 0 or n == 1:
            return True
        
        # Continua gerando números da sequência até encontrar ou ultrapassar o número informado
        while b < n:
            a, b = b, a + b
        
        # Verifica se o número informado é parte da sequência
        return b == n

    # Exemplo de uso
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_a_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if entrada == '3':

    # Função para calcular os valores solicitados
    def calcula_faturamento(file_path):
        # Lê o arquivo JSON com os dados de faturamento
        with open(file_path, 'r') as file:
            dados = json.load(file)

        # Extrai os valores de faturamento, ignorando os dias com valor zero
        valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

        # Calcula o menor e o maior valor de faturamento
        menor_valor = min(valores)
        maior_valor = max(valores)

        # Calcula a média de faturamento
        media_mensal = sum(valores) / len(valores)

        # Conta os dias com faturamento superior à média mensal
        dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

        # Retorna os resultados
        return menor_valor, maior_valor, dias_acima_da_media

    # Exemplo de uso
    file_path = 'desafio\\faturamento.json'
    menor, maior, dias_acima_media = calcula_faturamento(file_path)

    print(f"Menor valor de faturamento: {menor:.2f}")
    print(f"Maior valor de faturamento: {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    
if entrada == '4':
    # Dicionário com os valores de faturamento por estado
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    # Calcula o faturamento total da distribuidora
    faturamento_total = sum(faturamento_estados.values())

    # Calcula e imprime o percentual de representação de cada estado
    print("Percentual de representação de cada estado:")
    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")

if entrada == '5':
        # Definindo uma string de exemplo
    string = input("Informe uma string para inverter: ")

    # Função para inverter a string sem usar funções prontas
    def inverte_string(s):
        invertida = ''
        # Percorre a string de trás para frente
        for i in range(len(s) - 1, -1, -1):
            invertida += s[i]  # Adiciona cada caractere à nova string
        return invertida

    # Inverte a string informada
    string_invertida = inverte_string(string)

    # Exibe a string invertida
    print(f"String invertida: {string_invertida}")

