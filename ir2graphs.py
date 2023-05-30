from llhandler import LLHandler
import click
import os
import json
import importlib
from subdir import percorrer_subdiretorios

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--subdirectorys', '-s', is_flag=True, default=False, help='Iterate all subdirectories and search for .ll files.')
@click.option('--keepfolders', '-k', is_flag=True, default=False, help='Keep folders structure in output directory if --subdirectorys is True.')
@click.option('--costfunc', '-f', default="", help='Name of python file with cost function for array/matrix generation. Needs to be in same directory.')
@click.option('--regcost', '-r', default="", help='Path to .json file with the registers cost array.')
@click.option('--array', '-a', is_flag=True, default=False, help='Display cost array of nodes on .json file.')
@click.option('--matrix', '-m', is_flag=True, default=False, help='Display cost matrix of edges on .json file.')

def cli(dir, output, costfunc, regcost, array, matrix, subdirectorys, keepfolders):

    """Generate .json files with PBQP interference graphs from .ll files with mem2reg option"""
    
    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir

    if costfunc == "" or not os.path.isfile(costfunc):
        func = None
    else:
        nome_modulo = costfunc.split('.')[0]
        meu_modulo = importlib.import_module(nome_modulo, package=None)
        func = meu_modulo.costfunc

    if regcost == "" or not os.path.isfile(regcost):
        costArray = [0]*16
    else:
        with open(regcost) as json_file:
            costArray = json.load(json_file)

    if subdirectorys:
        # chama a função para percorrer todos os subdiretórios e salvar os caminhos em uma lista
        subdirs = percorrer_subdiretorios(dir)

        # loop para executar o comando com cada subdiretório como argumento
        for subdir in subdirs:
            if keepfolders:
                path_rel = os.path.relpath(subdir, dir)
                aux_dir = os.path.join(output, path_rel)
            else:
                aux_dir = output
            searchdir(subdir, aux_dir, func, costArray, array, matrix)
    searchdir(dir, output, func, costArray, array, matrix)
    

def searchdir(dir, output, costfunc, costArray, array, matrix):
    if not os.path.exists(output):
        os.makedirs(output)
    
    for file_name in os.listdir(dir):
        if file_name.endswith(".ll"):
            aux = file_name[:-3] + ".json"
            input_file_name = os.path.join(dir, file_name)
            output_file_name = os.path.join(output, aux)
            ir2graphs(input_file_name, output_file_name, costArray, array, matrix, costfunc)


def ir2graphs(inputfile, outputfile, costArray, arrayflag, edgeflag, costfunc):

    graphs = {}
    file = open(inputfile, "r")
    functions = LLHandler.read_llvm_ir_file(file)
    for function_name in functions:
        function_code = functions[function_name]
        vRegisters = LLHandler.analyze_registers(function_code)
        graph = LLHandler.create_graph(vRegisters, costArray, costfunc)
        if len(graph.edges) > 0:
            print(function_name + " : " + str(len(graph.nodes)) + " nodes and " + str(len(graph.edges)) + " edges\n")
            graphs[function_name] = graph

    with open(outputfile, "w") as f:
        f.write("{\n")
        flag = False
        for function_name in graphs:
            if flag:
                f.write(",\n")
            else:
                flag = True
            f.write("\t\"" + function_name + "\" : ")
            f.write(graphs[function_name].as_json(arrayflag, edgeflag, 1)) 
        f.write('\n}')

if __name__ == '__main__':
    cli()
    