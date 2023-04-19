def read_llvm_ir_file(filename):
    # Abrir o arquivo IR do LLVM e ler todas as linhas
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Inicializar o dicionário que irá armazenar os arrays de strings de cada função
    functions = {}

    # Percorrer todas as linhas do arquivo
    for i in range(len(lines)):
        line = lines[i].strip()

        # Verificar se a linha indica o início de uma nova função
        if line.startswith('define'):
            # Obter o nome da função a partir da linha de código
            function_name = line.split()[2]

            # Inicializar um novo array de strings para a função
            function_code = []

            # Adicionar cada linha de código subsequente da função até encontrar o final da função
            j = i + 1
            while j < len(lines) and not lines[j].startswith('}'):
                function_code.append(lines[j].strip())
                j += 1

            # Armazenar o array de strings da função no dicionário
            functions[function_name] = function_code

    # Retornar o dicionário contendo os arrays de strings de cada função
    return functions
