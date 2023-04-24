from llhandler import LLHandler
import sys
import json
import os

def ir2graphs(inputfile, outputfile, edgeflag):

    graphs = {}
    file = open(inputfile, "r")
    functions = LLHandler.read_llvm_ir_file(file)
    for function_name in functions:
        function_code = functions[function_name]
        vRegisters = LLHandler.analyze_registers(function_code)
        graph = LLHandler.create_graph(vRegisters, [0]*16)
        print(function_name + " : " + str(len(graph.nodes)) + " nodes and " + str(len(graph.edges)) + " edges\n")
        graphs[function_name] = graph.as_dict()

    with open(outputfile, "w") as f:
        f.write("{\n")
        flag = False
        for function_name in graphs:
            if flag:
                f.write(",\n")
            else:
                flag = True
            f.write("\"" + function_name + "\" :\n")
            
            nodes = graphs[function_name]["nodes"]
            f.write("\t{\n\t\"nodes\" :\n\t\t{\n")
            flag2 = False
            for node_name in nodes:
                if flag2:
                    f.write(",\n")
                else:
                    flag2 = True
                f.write("\t\t\"" + node_name + "\": " + str(nodes[node_name]))
            f.write("\n\t\t},\n")
            edges = graphs[function_name]["edges"]
            f.write("\t\"edges\" :\n\t\t[\n")

            flag3 = False
            for edge in edges:
                if flag3:
                    f.write(",\n")
                else:
                    flag3 = True
                f.write("\t\t{\"node 1\" : \"" + edge[0] +  "\",\n")
                f.write("\t\t\"node 2\" : \"" + edge[1] +  "\"")
                if edgeflag:
                    f.write(",\n\t\t\"cost matrix\" :\n")
                    f.write("\t\t\t[\n")
                    for arr in edge[2][:-1]:
                        f.write("\t\t\t" + json.dumps(arr) + ",\n")
                    f.write("\t\t\t" + json.dumps(edge[2][-1]) + "\n")
                    f.write("\t\t\t]")
                f.write("\n\t\t}")
            f.write("\t\t]\n")
            f.write("\t}")

        f.write('\n}\n')

    
if __name__ == '__main__':
    args_count = len(sys.argv)
    if args_count == 2:
        dir_path = os.getcwd()
        output_dir = dir_path
        edgeflag = bool(int(sys.argv[1]))
    elif args_count == 3:
        dir_path = os.getcwd()
        output_dir = sys.argv[1]
        edgeflag = bool(sys.argv[2])
    elif args_count == 4:
        dir_path = sys.argv[1]
        output_dir = sys.argv[2]
        edgeflag = bool(sys.argv[3])
    else:
        print("Error\n")
        quit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for input_file_name in os.listdir(dir_path):
        if input_file_name.endswith(".ll"):
            aux = input_file_name[:-3] + ".json"
            output_file_name = os.path.join(output_dir, aux)
            ir2graphs(input_file_name, output_file_name, edgeflag)
        
    