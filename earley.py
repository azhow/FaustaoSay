from copy import copy
import sys

class Rule:
    def __init__(self,var,d,*productions):
        self.var = var
        self.productions = list(productions)
        self.p = 0
        self.d = d
        
    def len(self):
        return len(self.productions)

    def __str__(self):
        # pra alguma coisa racket tinha que ter servido
        f = lambda x : '' if x == [] else x[0] + ' ' + f(x[1:])

        rule = str(self.var) + ' -> '
        rule += f(self.productions[:self.p])
        rule += u"\u2022"
        rule += f(self.productions[self.p:])
        rule += '/' + str(self.d)

        return rule
        
    def __eq__(self,other):
        var = self.var == other.var
        productions = self.productions == other.productions
        p = self.p == other.p
        d = self.d == other.p
        return var and productions and p and d



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


def earley(initial,variables,terminals,rules,string,printParse=False):
    D = [[] for _ in range(len(string.split())+1)]
    toDo = [initial]
    
    toParse = string.split()

    # cria D0
    while toDo != []:
        curVar = toDo[0]
        for productions in rules[curVar]:
            D[0].append(Rule(curVar,0,*productions))

            firstProduction = D[0][-1].productions[0]
            if firstProduction in variables and firstProduction not in toDo:
                toDo.append(firstProduction)
        toDo.pop(0)
        
    if printParse:
        print('S(0):')
        for x in D[0]:
            print(x)
        

    forceStop = False
    # faz o resto
    for i,word in enumerate(toParse):
        scan = [copy(rule) for rule in D[i] if (rule.productions[rule.p] == word if rule.p < rule.len() else False)]
        for rule in scan:
            rule.p += 1
            
        if scan != []:
            D[i+1].extend(scan)
            toDo = scan
            
            while toDo != []:
                curRule = toDo[0]
                if curRule.p >= curRule.len(): # complete
                    aux = [copy(rule) for rule in D[curRule.d] if (rule.productions[rule.p] == curRule.var if rule.p < rule.len() else False)]
                    for rule in aux:
                        rule.p += 1
                        if rule not in D[i+1]:
                            D[i+1].append(rule)
                        if rule not in toDo:
                            toDo.append(rule)
                
                elif curRule.productions[curRule.p] in variables: # predict
                    curVar = curRule.productions[curRule.p]
                    aux = [Rule(curVar,i+1,*productions) for productions in rules[curVar]]
                    D[i+1].extend(aux)
                    toDo.extend(aux)
            
                toDo.pop(0)
                
        else:   # cannot recognize
            forceStop = True
            break
            
        if printParse:
            print('\nS(' + str(i+1) + '):')
            for x in D[i+1]:
                print(x)
            
    recognized = False
    
    if not forceStop:
        for rule in D[-1]:
            if rule.var == initial and rule.p == rule.len() and rule.d == 0:
                recognized = True
                
    return recognized
        
        
    


if __name__ == '__main__':
    try:
        gramatica = sys.argv[1]
    except IndexError:
        print('Uso: ' + sys.argv[0] + ' gramatica')
        sys.exit(0)
    
    try:
        initial,variables,terminals,rules = read_file(gramatica)
    except FileNotFoundError:
        print('Arquivo ' + sys.argv[1] + ' não encontrado.')
        sys.exit(0)
    
    string = input('Frase a ser reconhecida (string vazia termina a execução): ')
    while string != '':
        print('\n\'' + string + '\' faz parte da linguagem.\n' 
            if earley(initial,variables,terminals,rules,string,True) 
            else '\n\'' + string + '\' não reconhecida como parte da linguagem.\n')
        string = input('Frase a ser reconhecida: ')   
         
