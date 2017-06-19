def read_file(file_path):
    proc = "Terminais"
    term = []
    varses = []
    ruuru = {}
    for line in open(file_path, 'rU'):
        if proc == "Terminais" and line.split('#')[0].strip().lower() != "terminais" and \
        line.split('#')[0].strip().lower() != "variaveis":
            term.append(line.split('[ ')[1].split(' ]')[0])

        elif proc == "Variaveis" and line.split('#')[0].strip().lower() != "inicial":
            varses.append(line.split('[ ')[1].split(' ]')[0])

        elif proc == "Inicial" and line.split('#')[0].strip().lower() != "regras":
            init = line.split('[ ')[1].split(' ]')[0]

        elif proc == "Regras":
            key = line.split(' > ')[0].strip().strip('[ ').strip(' ]')
            ruuru[key] = Production([x.strip().strip('[').strip(']').strip() for x in
                            line.split('>')[1].split('#')[0].split(';')[0].split('] [')], 0)

        else:
            proc = line.split('#')[0].strip()

    return term, varses, init, ruuru

class Production:
    def __init__(self, rule, p, pointer):
        self.p_list = p
        self.pointer = pointer

def predict():



def earley(w, G):




if __name__ == '__main__':
    print(read_file('./teste.txt'))
