from llhandler import LLHandler
import click
import os

@click.command()
@click.option('--dir', '-d', default="", help='Path to directory with .ll input files.')
@click.option('--output', '-o', default="", help='Path to output directory.')
@click.option('--array', '-a', is_flag=True, default=False, help='Display cost array of nodes on .json file.')
@click.option('--matrix', '-m', is_flag=True, default=False, help='Display cost matrix of edges on .json file.')

def cli(dir, output, array, matrix):
    
    if dir == "":
        dir = os.getcwd()
    
    if output == "":
        output = dir

    if not os.path.exists(output):
        os.makedirs(output)
    
    for file_name in os.listdir(dir):
        if file_name.endswith(".ll"):
            aux = file_name[:-3] + ".json"
            input_file_name = os.path.join(dir, file_name)
            output_file_name = os.path.join(output, aux)
            ir2graphs(input_file_name, output_file_name, array, matrix)

def ir2graphs(inputfile, outputfile, arrayflag, edgeflag):

    graphs = {}
    file = open(inputfile, "r")
    functions = LLHandler.read_llvm_ir_file(file)
    for function_name in functions:
        function_code = functions[function_name]
        vRegisters = LLHandler.analyze_registers(function_code)
        graph = LLHandler.create_graph(vRegisters, [0]*16, None)
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
    