class Rule:
    def __init__(self,var,d,*productions):
        self.var = var
        self.productions = list(productions)
        self.p = 0
        self.d = d

    def __str__(self):
        # pra alguma coisa racket tinha que ter servido
        f = lambda x : '' if x == [] else x[0] + ' ' + f(x[1:])

        rule = str(self.var) + ' -> '
        rule += f(self.productions[:self.p])
        rule += '*'
        rule += f(self.productions[self.p:])
        rule += '/' + str(self.d)

        return rule



def read_file(file_path):
    """
    Reads the grammar file contents.
        In:
            file_path:string = File path.
        Out:
            initial_D:string = Initial rule of the grammar.
            ruurus:smt = Rules of the grammar.
    """
    proc = ''

    initial_D = ''
    variables = []
    terminals = []
    rules = {}

    for line in open(file_path, "rU"):
        if proc == "Terminais" and line.split('#')[0].strip() != "Terminais" and \
        line.split('#')[0].strip() != "Variaveis":
            terminals.append(line.split('[ ')[1].split(' ]')[0])
        elif proc == "Variaveis" and line.split('#')[0].strip() != "Inicial":
            key = line.split('[')[1].split(']')[0].strip()
            variables.append(key)
            rules[key] = []
        elif proc == "Inicial" and line.split('#')[0].strip() != "Regras":
            # Reads the initial for the parsing start
            initial_D = line.split("#")[0].strip().strip(" ]").strip("[ ")
            proc = ""
        elif proc == "Regras":
            # Build rules and productions following stuff from l.19x
            key = line.split('>')[0].strip().strip('[').strip(']').strip()
            rules[key].append([x for x in \
                line.split('>')[1].split('#')[0].split(';')[0]\
                .strip().strip('[ ').strip(' ]').split(' ] [ ')])
        else:
            proc = line.split('#')[0].strip()

    return initial_D,variables,terminals,rules


def earley(initial,variables,terminals,rules,string):
    D = [[]]
    toDo = [initial]

    #cria D0
    while toDo != []:
        curVar = toDo[0]
        for productions in rules[curVar]:
            D[0].append(Rule(curVar,0,*productions))

            firstProduction = D[0][-1].productions[0]
            if firstProduction in variables and firstProduction not in toDo:
                toDo.append(firstProduction)
        toDo.pop(0)
    #for x in D[0]:
    #    print(x)

    #TODO o resto


if __name__ == '__main__':
    initial,variables,terminals,rules = read_file('gramatica.gr')
    earley(initial,variables,terminals,rules,'')
