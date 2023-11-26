#!/usr/bin/env python3

import sys
import argparse
import os.path
import earley

import importlib.util
playsound_spec = importlib.util.find_spec('playsound')
has_audio = playsound_spec is not None


def create_parser():
    return parser


def handle_audio(sentence, audio_dir):
    module = importlib.util.module_from_spec(playsound_spec)
    sys.modules['playsound'] = module
    playsound_spec.loader.exec_module(module)

    audio_dir = os.path.abspath(audio_dir)
    audio_files = []
    for word in sentence.split():
        audio_file_path = audio_dir + '/' + word + '.wav'
        if not os.path.isfile(audio_file_path):
            print(parser.prog + ': error: missing audio file for terminal ' + word + '.')
            return False

        audio_files.append(audio_file_path)

    for audio_file in audio_files:
        module.playsound(audio_file)

    return True


def main(grammar_file, audio_dir=""):
    if not os.path.isfile(grammar_file):
        print('Error: file ' + grammar_file + ' not found.')
        return -1

    if len(audio_dir) != 0 and not os.path.isdir(audio_dir):
        print(parser.prog + ': error: directory ' + audio_dir + ' not found.')
        return -2

    initial, variables, terminals, rules = earley.read_file(grammar_file)

    sentence = earley.generate_random(
        initial, variables, terminals, rules, False)

    if len(audio_dir) != 0 and has_audio:
        if not handle_audio(sentence, audio_dir):
            return -3

    print(sentence)

    return 0


if __name__ == '__main__':
    grammar_file = os.path.dirname(__file__) + '/grammars/fausto.gr'
    audio_dir = ""

    if len(sys.argv) != 1:
        parser = argparse.ArgumentParser(
            description='Sentence generator: \
                         generates a sentence from the language \
                         described in given grammar file.')
        parser.add_argument(
            'grammar', help='path to file containing the grammar to be used')
        parser.add_argument(
            '-f', metavar='path',
            help='path to directory containing \
                  .wav files named accordingly \
                  with the terminal they represent')

        args = parser.parse_args()
        grammar_file = args.grammar
        audio_dir = args.f

    ret_code = main(grammar_file, audio_dir)
    sys.exit(ret_code)
