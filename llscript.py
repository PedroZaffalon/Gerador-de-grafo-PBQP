import os
import subprocess
import click

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--clean', '-c', is_flag=True, default=True, help='Remove temporary .ll files.')


def cli(dir, output, clean):

    """Compile c/c++ codes on directory and generates .ll files with mem2reg option"""

    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir
    
    # Primeiro, definimos a linha de comando que será executada para cada arquivo .c
    c_command = "clang -Xclang -disable-O0-optnone -S -emit-llvm {} -o {}.ll"

    # Em seguida, iteramos sobre todos os arquivos .c no diretório
    for file_name in os.listdir(dir):
        if file_name.endswith(".c"):
            # Executamos a linha de comando para cada arquivo .c
            input_file_name = os.path.join(dir, file_name)
            command = c_command.format(input_file_name, input_file_name[:-2])
            subprocess.run(command, shell=True)
    
    # Certificamo-nos de que o diretório de saída existe; se não, criamos um
    if not os.path.exists(output):
        os.makedirs(output)

    # Definimos a linha de comando para gerar os arquivos .ll de saída
    ll_command = "opt -S -mem2reg {}.ll -o {}.ll"

    # Iteramos sobre todos os arquivos .ll gerados pelo comando anterior
    for file_name in os.listdir(dir):
        if file_name.endswith(".ll"):
            # Executamos a linha de comando para cada arquivo .ll
            input_file_name = os.path.join(dir, file_name[:-3])
            output_file_name = os.path.join(output, file_name[:-3])
            command = ll_command.format(input_file_name, output_file_name)
            subprocess.run(command, shell=True)
            if clean:
                os.remove(input_file_name + ".ll")

if __name__ == '__main__':
    cli()