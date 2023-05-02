import os
import subprocess
import click
import llscript

@click.command()
@click.option('--dir', '-d', default="", help='Path to root directory.')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--clean', '-c', is_flag=True, default=True, help='Remove temporary .ll files.')
@click.option('--name', '-n', default="", help='Name for output files. Files name will be:  "name_0", "name_2", "name_3" ... "name_[number_of_files]". Default is original files names.')

def cli(dir, output, clean, name):

    """Iterate all subdirectories and execute the llscript."""

    if dir == "":
        dir = os.getcwd()

    # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista
    subdirs = percorrer_subdiretorios(dir)

    i = 1

    # loop para executar o comando com cada subdiretório como argumento
    for subdir in subdirs:
        i = llscript.llscript(subdir, output, clean, name, i)


# função para percorrer recursivamente todos os subdiretórios da pasta raiz e salvar os caminhos em uma lista
def percorrer_subdiretorios(root_dir):
    # lista para armazenar os caminhos dos subdiretórios
    subdirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # para cada subdiretório encontrado, adicione o caminho à lista
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdirs.append(subdir_path)
    return subdirs

if __name__ == '__main__':
    cli()