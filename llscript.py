import os
import subprocess
import sys

def generatell(dir_path, output_dir):
    # Primeiro, definimos a linha de comando que será executada para cada arquivo .c
    c_command = "clang -S -emit-llvm {} -o {}.ll"

    # Em seguida, iteramos sobre todos os arquivos .c no diretório
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".c"):
            # Executamos a linha de comando para cada arquivo .c
            command = c_command.format(file_name, file_name[:-2])
            subprocess.run(command, shell=True)
    
    # Certificamo-nos de que o diretório de saída existe; se não, criamos um
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definimos a linha de comando para gerar os arquivos .ll de saída
    ll_command = "opt -mem2reg {}.ll -o {}/{}.bc"

    # Iteramos sobre todos os arquivos .ll gerados pelo comando anterior
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".ll"):
            # Executamos a linha de comando para cada arquivo .ll
            command = ll_command.format(file_name[:-3], output_dir, file_name[:-3])
            subprocess.run(command, shell=True)

if __name__ == '__main__':
    args_count = len(sys.argv)
    if args_count == 1:
        dir_path = os.getcwd()
        output_dir = dir_path
    elif args_count == 2:
        dir_path = os.getcwd()
        output_dir = sys.argv[2]
    elif args_count == 4:
        dir_path = sys.argv[1]
        output_dir = sys.argv[2]
    else:
        print("Error\n")
        quit(1)
    
    generatell(dir_path, output_dir)
    