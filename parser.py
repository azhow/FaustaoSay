import argparse
import earley

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sentence parser: \
                                                  returns if given sentences are part of the \
                                                  language described in given grammar file.')
    parser.add_argument('grammar', help='path to file containing the grammar to be used')
    parser.add_argument('-v', '--verbose', action='store_true', help='print parsing steps')
    args = parser.parse_args()
    
    initial, variables, terminals, rules = earley.read_file(args.grammar)
    
    string = input('Frase a ser reconhecida (string vazia termina a execução): ')
    while string != '':
        print('\n\'' + string + '\' faz parte da linguagem.\n'
              if earley.earley(initial, variables, rules, string, args.verbose)
              else '\n\'' + string + '\' não reconhecida como parte da linguagem.\n')
        string = input('Frase a ser reconhecida: ')