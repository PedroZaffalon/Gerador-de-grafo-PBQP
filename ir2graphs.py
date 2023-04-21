from llhandler import LLHandler
import sys
import json

if __name__ == '__main__':
    args_count = len(sys.argv)
    if args_count > 3:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
    elif args_count < 3:
        print("You must specify the file path")
        raise SystemExit(2)

    try:
        file = open(sys.argv[1], "r")
    except:
        print("The file doesn't exist")
        raise SystemExit(1)
    
    graphs = {}

    functions = LLHandler.read_llvm_ir_file(file)
    for function_name in functions:
        function_code = functions[function_name]
        vRegisters = LLHandler.analyze_registers(function_code)
        graph = LLHandler.create_graph(vRegisters, [0]*16)

        graphs[function_name] = graph.as_dict()

    with open(sys.argv[2], "w") as f:
        f.write("{\n")
        for function_name in graphs:
            f.write("\"" + function_name + "\" :\n")
            
            nodes = graphs[function_name]["nodes"]
            f.write("\t{\n\t\"nodes\" :\n\t\t{\n")
            for node_name in nodes:
                f.write("\t\t\"" + node_name + "\": " + str(nodes[node_name]) + ",\n")
            f.write("\t\t},\n")
            edges = graphs[function_name]["edges"]
            f.write("\t\"edges\" :\n\t\t{\n")
            for edge in edges:
                f.write("\t\t\"node 1\" : \"" + edge[0] +  "\",\n")
                f.write("\t\t\"node 2\" : \"" + edge[1] +  "\",\n")
                f.write("\t\t\"cost matrix\" :\n")
                f.write("\t\t\t[\n")
                for arr in edge[2]:
                    f.write("\t\t\t" + json.dumps(arr) + ",\n")
                f.write("\t\t\t],\n")
            f.write("\t\t},\n")
            f.write("\t},\n")

        f.write('}\n')

    

        
    