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
                # I stole this line bc I was having problems with printing some of the goofy chars
            
            case '[':
                if cells[ccell] > 0:
                    loop += char
            
            case ']':
                if cells[ccell] == 0:
                # So I think this is wrong—the cell I need to check is 
                # the one the loop started in iirc. Which shouldn't be hard to
                # implement, I just don't remember how BF works
                    loop = ''
                else:
                    ccell, cells = interpret(loop, ccell, cells)
                    # This could and probably will lead to a stack overflow but idk what else to do

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