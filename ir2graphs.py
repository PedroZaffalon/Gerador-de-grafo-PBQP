from llhandler import LLHandler
import sys
import os

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
    args_count = len(sys.argv)
    if args_count == 2:
        dir_path = os.getcwd()
        output_dir = dir_path
        edgeflag = bool(int(sys.argv[1]))
    elif args_count == 3:
        dir_path = os.getcwd()
        output_dir = sys.argv[1]
        edgeflag = bool(int(sys.argv[2]))
    elif args_count == 4:
        dir_path = sys.argv[1]
        output_dir = sys.argv[2]
        edgeflag = bool(int(sys.argv[3]))
    else:
        print("Error\n")
        quit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".ll"):
            aux = file_name[:-3] + ".json"
            input_file_name = os.path.join(dir_path, file_name)
            output_file_name = os.path.join(output_dir, aux)
            ir2graphs(input_file_name, output_file_name, 1, edgeflag)
        
    