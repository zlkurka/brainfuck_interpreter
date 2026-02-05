import sys

def get_code():
    program = open("program.txt")
    code = program.read()
    program.close()
    return code

def interpret(code, ccell, cells):
    
    loop = ''
    
    for char in code:
        
        if loop:
            loop += char
        
        match char:
            
            case '>':
                ccell += 1
                if len(cells) - 1 < ccell:
                    cells.append(0)
            
            case '<':
                if ccell > 0:
                    ccell -= 1
            
            case '+':
                if cells[ccell] == 255:
                    cells[ccell] = 0
                else:
                    cells[ccell] += 1

            case '-':
                if cells[ccell] == 0:
                    cells[ccell] = 255
                else:
                    cells[ccell] -= 1
            
            case '.':
                sys.stdout.write(chr(cells[ccell]))
            
            case '[':
                if cells[ccell] > 0:
                    loop += char
            
            case ']':
                if cells[ccell] == 0:
                    loop = ''
                else:
                    ccell, cells = interpret(loop, ccell, cells)

            case ',':
                cells[ccell] = input()
                # TODO figure this out
            
            case _:
                pass
            
    return ccell, cells

def main():
    
    code = get_code()
    
    ccell = 0
    cells = [0]

    ccell, cells = interpret(code, ccell, cells)
    print()

main()