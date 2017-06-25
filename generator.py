import sys
import argparse
import os.path
import earley

hasAudio = True
try:
    import pyglet
except ModuleNotFoundError:
    hasAudio = False
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sentence generator: \
                                                  generates a sentence from the language \
                                                  described in given grammar file.')
    parser.add_argument('grammar', help='path to file containing the grammar to be used')
    parser.add_argument('-v', '--verbose', action='store_true', help='print parsing steps')
    parser.add_argument('-f', metavar='path', help='path to directory containing \
                                                    .wav files named accordingly \
                                                    with the terminal they represent')
    args = parser.parse_args()
    
    
    
    if os.path.isfile(args.grammar):
        initial, variables, terminals, rules = earley.read_file(args.grammar)
    else:
        print(parser.prog + ': error: file ' + args.grammar + ' not found.')
        sys.exit(-1)
        
    playAudio = False
    if args.f:
        if os.path.isdir(args.f):
            playAudio = True
        else:
            print(parser.prog + ': error: directory ' + args.f + ' not found.')
            sys.exit(-2)
            
    
    
    frase = earley.generate_random(initial, variables, terminals, rules, args.verbose)
    if args.verbose:
        print('\nFrase gerada: ', end='')
    print(frase)
    
    
    if playAudio and hasAudio:
        audioDir = os.path.abspath(args.f)
        audios = {}
        player = pyglet.media.Player()
        
        for word in frase.split():
            if os.path.isfile(audioDir + '/' + word + '.wav'):
                player.queue(audioDir + '/' + word + '.wav')
            else:
                print(parser.prog + ': error: missing audio file for terminal ' + word + '.')
                sys.exit(-3)
        
        player.play()