import dis

def print_names(filename):
    with open(filename, 'rb') as file:
        bytecode = file.read()
        instructions = dis.get_instructions(bytecode)
        names = {instr.argval for instr in instructions if instr.opname == 'LOAD_CONST'}
        
        for name in sorted(names):
            if not name.startswith('__'):
                print(name)

if __name__ == "__main__":
    print_names("hidden_4.pyc")
