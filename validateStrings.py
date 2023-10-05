import click
import os
from subdir import percorrer_subdiretorios

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--subdirectorys', '-s', is_flag=True, default=False, help='Iterate all subdirectories and search for .ll files.')
def cli(dir, subdirectorys):

    """Correct the strings in JSON graph files"""
    if dir == "":
        dir = os.getcwd()
    
    if subdirectorys:
        # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista 
        subdirs = percorrer_subdiretorios(dir)

        # loop para executar o comando com cada subdiretório como argumento
        for subdir in subdirs:
            print("\n" + subdir + "\n")
            searchjson(subdir, True)         
    print("\n" + dir + ":\n")
    searchjson(dir, True)

def searchjson(dir, flag):
    for file_name in os.listdir(dir):
        if file_name.endswith(".json"):
            input_file_name = os.path.join(dir, file_name)
            if flag:
                print(file_name)
            modify_json_file(input_file_name)
            

def modify_json_file(input_file):
    with open(input_file, 'r') as f:
        data = f.read()

    modified_data = ''
    flag = False

    for i in range(len(data)):
        char = data[i]
        if char == '"':
            if not flag:
                flag = True
            else:
                char1 = data[i + 1]
                char2 = data[i + 2]
                if char1 == '\n' or (char1 == ' ' and char2 == ':') or (char1 == ',' and char2 == '\n'):
                    flag = False
                else:
                    modified_data += '\\'
        modified_data += char

    with open(input_file, 'w') as f:
        f.write(modified_data)

if __name__ == '__main__':
    cli()