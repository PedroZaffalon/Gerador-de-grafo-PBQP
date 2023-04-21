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
        file = open(args_count[1])
    except:
        print("The file doesn't exist")
        raise SystemExit(1)
    
    graphs = {}

    functions = LLHandler.read_llvm_ir_file(file)
    for function_name in functions:
        function_code = functions[function_name]
        vRegisters = LLHandler.analyze_register(function_code)
        graph = LLHandler.create_graph(vRegisters, [0]*16)
        graphs[function_name] = graph.as_dict()

    with open(args_count[2], "w") as f:
        json.dump(graphs, f, indent=4)
    

        
    