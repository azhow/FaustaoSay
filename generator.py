#!/usr/bin/env python3

import sys
import argparse
import os.path
import earley
import wave

hasAudio = True
try:
    import pyaudio
except ImportError:
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
        p = pyaudio.PyAudio()
        audioFiles = []
        for word in frase.split():
            audioPath = audioDir + '/' + word + '.wav'
            if os.path.isfile(audioPath):
                audioFiles.append(wave.open(audioPath,"rb"))
            else:
                print(parser.prog + ': error: missing audio file for terminal ' + word + '.')
                sys.exit(-3)
                
        for audioFile in audioFiles:
            chunk = 1024
            stream = p.open(format=p.get_format_from_width(audioFile.getsampwidth()),  
                            channels=audioFile.getnchannels(),  
                            rate=audioFile.getframerate(),  
                            output=True)
            data = audioFile.readframes(chunk)
            while data:
                stream.write(data)  
                data = audioFile.readframes(chunk)
            stream.stop_stream()  
            stream.close()
        p.terminate() 