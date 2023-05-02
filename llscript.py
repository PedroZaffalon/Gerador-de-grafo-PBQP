import os
import subprocess
import click

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--clean', '-c', is_flag=True, default=True, help='Remove temporary .ll files.')
@click.option('--name', '-n', default="", help='Name for output files. Files name will be:  "name_0", "name_2", "name_3" ... "name_[number_of_files]". Default is original files names.')

def cli(dir, output, clean, name):

    """Compile c/c++ codes on directory and generates .ll files with mem2reg option"""

    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir
    
    llscript(dir, output, clean, name, 1)


    
def llscript(dir, output, clean, name, n_start):
    # Primeiro, definimos a linha de comando que será executada para cada arquivo .c
    c_command = "clang -Xclang -disable-O0-optnone -S -emit-llvm {} -o {}.ll"

    # Em seguida, iteramos sobre todos os arquivos .c no diretório
    i = n_start
    for file_name in os.listdir(dir):
        if file_name.endswith(".c") or file_name.endswith(".cpp"):
            # Executamos a linha de comando para cada arquivo .c
            if name != "":
                aux_name = name + "_" + str(i)
            else:
                aux_name = file_name.split('.')[0]
            input_file_name = os.path.join(dir, file_name)
            output_file_name = os.path.join(dir, aux_name)
            command = c_command.format(input_file_name, output_file_name)
            subprocess.run(command, shell=True)
            i += 1
    
    # Certificamo-nos de que o diretório de saída existe; se não, criamos um
    if not os.path.exists(output):
        os.makedirs(output)

    # Definimos a linha de comando para gerar os arquivos .ll de saída
    ll_command = "opt -S -mem2reg {}.ll -o {}.ll"

    # Iteramos sobre todos os arquivos .ll gerados pelo comando anterior
    i = n_start
    for file_name in os.listdir(dir):
        if file_name.endswith(".ll"):
            
            if name != "":
                aux_name = name + "_" + str(i)
            else:
                aux_name = file_name.split('.')[0]

            input_file_name = os.path.join(dir, file_name[:-3])
            output_file_name = os.path.join(output, aux_name)
            command = ll_command.format(input_file_name, output_file_name)
            subprocess.run(command, shell=True)
            if clean:
                os.remove(input_file_name + ".ll")
            i += 1

    return i



if __name__ == '__main__':
    cli()