import os
import subprocess
import click
from subdir import percorrer_subdiretorios

@click.command()
@click.option('--dir', '-d', default="", help='Path to root directory for C/C++ files search')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--subdirectorys', '-s', is_flag=True, default=False, help='Iterate all subdirectories and search for C/C++ files.')
@click.option('--keepfolders', '-k', is_flag=True, default=False, help='Keep folders structure in output directory if --subdirectorys is True.')
@click.option('--temporary', '-t', is_flag=True, default=False, help='Do not remove temporary .ll files.')
@click.option('--name', '-n', default="", help='Name for output files. Files name will be:  "name_0", "name_2", "name_3" ... "name_[number_of_files]". Default is original files names.')

def cli(dir, output, temporary, name, subdirectorys, keepfolders):

    """Compile c/c++ codes on directory and generates .ll files with mem2reg option"""

    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir

    if subdirectorys:
        # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista
        subdirs = percorrer_subdiretorios(dir)

        i = 1

        # loop para executar o comando com cada subdiretório como argumento
        for subdir in subdirs:
            if keepfolders:
                path_rel = os.path.relpath(subdir, dir)
                aux_dir = os.path.join(output, path_rel)
                i = 1
            else:
                aux_dir = output
            i = llscript(subdir, aux_dir, temporary, name, i)
    
    llscript(dir, output, temporary, name, 1)


    
def llscript(dir, output, temporary, name, n_start):
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
            if not temporary and output != dir:
                os.remove(input_file_name + ".ll")
            i += 1

    return i

if __name__ == '__main__':
    cli()