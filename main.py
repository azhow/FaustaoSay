def read_file(file_path):
    proc = "Terminais"
    term = []
    varses = []
    ruuru = {}
    for line in open(file_path, 'rU'):
        if proc == "Terminais" and line.split('#')[0].strip().lower() != "terminais" and \
        line.split('#')[0].strip().lower() != "variaveis":
            term.append(line.split('[')[1].split(']')[0].strip())

        elif proc == "Variaveis" and line.split('#')[0].strip().lower() != "inicial":
            varses.append(line.split('[')[1].split(']')[0].strip())

        elif proc == "Inicial" and line.split('#')[0].strip().lower() != "regras":
            init = line.split('[')[1].split(']')[0].strip()

        elif proc == "Regras":
            key = line.split('>')[0].strip().strip('[').strip(']').strip()
            ruuru[key] = [x.strip().strip('[').strip(']').strip() for x in
                            line.split('>')[1].split('#')[0].split(';')[0].split('] [')]

        else:
            proc = line.split('#')[0].strip()

    return term, varses, init, ruuru

if __name__ == '__main__':
    print(read_file('./teste.txt'))
