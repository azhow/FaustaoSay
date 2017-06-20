def fun(line, key, terms, ruuru):
    for x in line.split('>')[1].split('#')[0].split(';')[0].split('] ['):
        if key in terms:
            x.strip().strip('[').strip(']').strip()
        else:
            ruuru[x.strip().strip('[').strip(']').strip()


def read_file(file_path):
    """ Reads the grammar file contents.
        In:
            file_path:string = File path.
        Out:
            initial_D:string = Initial rule of the grammar.
            ruurus:smt = Rules of the grammar.
    """
    proc = ""
    initial_D = ""
    ruuru = {}
    terms = []
    for line in open(file_path, "rU"):
        if proc == "Terminais" and line.split('#')[0].strip() != "Terminais" and \
        line.split('#')[0].strip() != "Variaveis":
            terms.append(line.split('[ ')[1].split(' ]')[0])
        elif proc == "Variaveis" and line.split('#')[0].strip() != "Inicial":
            key = line.split('[')[1].split(']')[0].strip()
            ruuru[key] = Rule(key, *[])
        elif proc == "Inicial" and line.split('#')[0].strip() != "Regras":
            # Reads the initial for the parsing start
            initial_D = line.split("#")[0].strip().strip(" ]").strip("[ ")
            proc = ""
        elif proc == "Regras":
            # Build rules and productions following stuff from l.19x
            key = line.split('>')[0].strip().strip('[').strip(']').strip()
            ruuru[key].productions.append(Production(*[x.strip().strip('[').strip(']').strip() if key in terms else
                                    ruuru[x.strip().strip('[').strip(']').strip()] for x in
                                    line.split('>')[1].split('#')[0].split(';')[0].split('] [')]))
        else:
            proc = line.split('#')[0].strip()

    return initial_D, ruuru, terms

class Production(object):
    def __init__(self, *terms):
        self.terms = terms
    def __len__(self):
        return len(self.terms)
    def __getitem__(self, index):
        return self.terms[index]
    def __iter__(self):
        return iter(self.terms)
    def __repr__(self):
        return " ".join(str(t) for t in self.terms)
    def __eq__(self, other):
        if not isinstance(other, Production):
            return False
        return self.terms == other.terms
    def __ne__(self, other):
        return not (self == other)
    def __hash__(self):
        return hash(self.terms)

class Rule(object):
    def __init__(self, name, *productions):
        self.name = name
        self.productions = list(productions)
    def __str__(self):
        return self.name
    def __repr__(self):
        return ("{0} -> {1}".format(self.name, " | ".join(repr(p) for p in self.productions)))
    def add(self, *productions):
        self.productions.extend(productions)

class State(object):
    def __init__(self, name, production, dot_index, start_column):
        self.name = name
        self.production = production
        self.start_column = start_column
        self.end_column = None
        self.dot_index = dot_index
        self.rules = [t for t in production if isinstance(t, Rule)]
    def __repr__(self):
        terms = [str(p) for p in self.production]
        terms.insert(self.dot_index, u"$")
        return ("{0:5} -> {1:16} [{2}-{3}]".format(self.name, " ".join(terms), self.start_column, self.end_column))
    def __eq__(self, other):
        return (self.name, self.production, self.dot_index, self.start_column) == \
            (other.name, other.production, other.dot_index, other.start_column)
    def __ne__(self, other):
        return not (self == other)
    def __hash__(self):
        return hash((self.name, self.production))
    def completed(self):
        return self.dot_index >= len(self.production)
    def next_term(self):
        if self.completed():
            return None
        return self.production[self.dot_index]

class Column(object):
    def __init__(self, index, token):
        self.index = index
        self.token = token
        self.states = []
        self._unique = set()
    def __str__(self):
        return str(self.index)
    def __len__(self):
        return len(self.states)
    def __iter__(self):
        return iter(self.states)
    def __getitem__(self, index):
        return self.states[index]
    def enumfrom(self, index):
        for i in range(index, len(self.states)):
            yield i, self.states[i]
    def add(self, state):
        if state not in self._unique:
            self._unique.add(state)
            state.end_column = self
            self.states.append(state)
            return True
        return False
    def print_(self, completedOnly = False):
        print("[{0}] {1}".format(self.index, self.token))
        print("=" * 35)
        for s in self.states:
            if completedOnly and not s.completed():
                continue
            print(repr(s))
        print()

class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def print_(self, level = 0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.print_(level + 1)

def predict(col, rule):
    for prod in rule.productions:
        col.add(State(rule.name, prod, 0, col))

def scan(col, state, token):
    if token != col.token:
        return
    col.add(State(state.name, state.production, state.dot_index + 1, state.start_column))

def complete(col, state):
    if not state.completed():
        return
    for st in state.start_column:
        term = st.next_term()
        if not isinstance(term, Rule):
            continue
        if term.name == state.name:
            col.add(State(st.name, st.production, st.dot_index + 1, st.start_column))

GAMMA_RULE = u"GAMMA"

def parse(rule, text):
    table = [Column(i, tok) for i, tok in enumerate([None] + text.lower().split())]
    table[0].add(State(GAMMA_RULE, Production(rule), 0, table[0]))

    for i, col in enumerate(table):
        for state in col:
            if state.completed():
                complete(col, state)
            else:
                term = state.next_term()
                if isinstance(term, Rule):
                    predict(col, term)
                elif i + 1 < len(table):
                    scan(table[i+1], state, term)

        #col.print_(completedOnly = True)

    # find gamma rule in last table column (otherwise fail)
    for st in table[-1]:
        if st.name == GAMMA_RULE and st.completed():
            return st
    else:
        raise ValueError("parsing failed")

def build_trees(state):
    return build_trees_helper([], state, len(state.rules) - 1, state.end_column)

def build_trees_helper(children, state, rule_index, end_column):
    if rule_index < 0:
        return [Node(state, children)]
    elif rule_index == 0:
        start_column = state.start_column
    else:
        start_column = None

    rule = state.rules[rule_index]
    outputs = []
    for st in end_column:
        if st is state:
            break
        if st is state or not st.completed() or st.name != rule.name:
            continue
        if start_column is not None and st.start_column != start_column:
            continue
        for sub_tree in build_trees(st):
            for node in build_trees_helper([sub_tree] + children, state, rule_index - 1, st.start_column):
                outputs.append(node)
    return outputs

"""
N = Rule("N", Production("time"), Production("flight"), Production("banana"),
    Production("flies"), Production("boy"), Production("telescope"))
D = Rule("D", Production("the"), Production("a"), Production("an"))
V = Rule("V", Production("book"), Production("eat"), Production("sleep"), Production("saw"))
P = Rule("P", Production("with"), Production("in"), Production("on"), Production("at"),
    Production("through"))

PP = Rule("PP")
NP = Rule("NP", Production(D, N), Production("john"), Production("houston"))
NP.add(Production(NP, PP))
PP.add(Production(P, NP))

VP = Rule("VP", Production(V, NP))
VP.add(Production(VP, PP))
S = Rule("S", Production(NP, VP), Production(VP))

for tree in build_trees(parse(S, "book the flight through houston")):
    print("--------------------------")
    tree.print_()
"""
if __name__ == "__main__":
    print(read_file(input("File to be read")))
    #init, ruurus, terms = read_file(input("File to be read: "))
    """ Kinda the structure we need
    if init and ruurus:
        to_parse = input("String to parse: ")
        for tree in build_trees(parse(init, to_parse))
        print("----------------------------------------------------")
        tree.print_()
    """
