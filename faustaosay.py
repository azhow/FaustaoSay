#!/usr/bin/env python3
import sys


def generate_message_balloon(input_string, max_string_length):
    bal = ''
    bal += '  ' + '_' * (max_string_length + 1) + '\n'

    # Handle single line strings
    if len(input_string) <= max_string_length:
        bal += '< ' + input_string.ljust(max_string_length) + ' >' + '\n'
    # Handle multi line input
    else:
        i = 0
        while True:
            start_idx = i * max_string_length
            end_idx = (i * max_string_length) + max_string_length
            line = input_string[start_idx:end_idx]
            message_part = line.ljust(max_string_length)
            if message_part[max_string_length - 1] not in [' ', ',']:
                message_part += '-'
            else:
                message_part += ' '

            if i == 0:
                bal += '/ ' + message_part + ' \\' + '\n'
            elif len(line) < max_string_length:
                bal += '\\ ' + message_part + ' /' + '\n'
                break
            else:
                bal += '| ' + message_part + ' |' + '\n'
            i += 1

    bal += '  ' + '-' * (max_string_length + 1) + '\n'
    bal += ' ' * 9 + '\\' + '\n'
    bal += ' ' * 10 + '\\'

    return bal


def faustao():
    fausto = '           `-/syddhhyhhhddhhsys+/:.                ' + '\n'
    fausto += '      `///ohdmmmdmmdddmmNNNmmmmmdddy+.             ' + '\n'
    fausto += '     -hyssydmNNNNmmmmmmNNNNNNNNNNmddhhs.           ' + '\n'
    fausto += '    -dddhdhdmNNMMMMMMMMNNNNNNNmmNNNNmhyy+`         ' + '\n'
    fausto += '   .dmddmmNNNMNNNNNNNNMMNNNNNmddmmNNNNmmdh/        ' + '\n'
    fausto += '   dmNdmdmNNNmmmmdhhhhsyyyyyyyhhdmmNNNNNNmdy`      ' + '\n'
    fausto += '  +mmmNNNmhyyso+o/::-......---::/+shNNmmdmmmd`     ' + '\n'
    fausto += ' .NNNNMNmo/:.....`````````````````.-+hmmmmdhhs     ' + '\n'
    fausto += ' -MMNMNh+:-..```````````````````````.-smNNNNmm+    ' + '\n'
    fausto += ' +MMMNh:...```````````````````````````./hmNMNNN/   ' + '\n'
    fausto += ' /NNNm+-...`````````````````````````` ``-yNNMNNN.  ' + '\n'
    fausto += ' hMNNy/-..````````````````....-:/oo/+/-.`.+mNMNN/  ' + '\n'
    fausto += ' sMNNh+-.......````````..-:/osydy+:--:::.``omNMN:  ' + '\n'
    fausto += ' /MMNh/...-://++++/:-::---+syys/+///++---.`-hmNh-  ' + '\n'
    fausto += ' -NMNh-.:+ossyyhhhhyso/---:ohsyysddyo+:-..`.odd+/` ' + '\n'
    fausto += '  yNNh--++:-:////oshdy/....:oo++/::--..````.:ss:/` ' + '\n'
    fausto += '  :NNh--:-/hhyyhdhsyss/-.`.-........``````.../+:-` ' + '\n'
    fausto += '   oNm:-::::://///:----.`````....`````````.......` ' + '\n'
    fausto += '   .mms---.....``...-:-.`````./o+/--............`` ' + '\n'
    fausto += '    .hd:----..```..:++--..-.-/+ooos+//::----......`' + '\n'
    fausto += '     /d:------..-:/sy+syyyyyhs+///oyyso+/::--....:`' + '\n'
    fausto += '      -----:::::/+yyoooosyyso/::::+oyhyo/:::---..- ' + '\n'
    fausto += '      .--:::///+oyysoo//::--:///osyddds+/::::-----`' + '\n'
    fausto += '      .--:://++oyhysssossyyss+soshho+so/:::::-----`' + '\n'
    fausto += '      `--::///+//shhdmNmhyo+oso///:--:+//::::----. ' + '\n'
    fausto += '      `--:::::/::/++++oo+/:::::--------:/://:::--` ' + '\n'
    fausto += '       .::::::::--:::::///:/:::----....:///:::--.  ' + '\n'
    fausto += '        -:::::///:-::--:::--..........-:////:---   ' + '\n'
    fausto += '        `-::::://+//::------.......---:///:::--`   ' + '\n'
    fausto += '         `-::::::///++:---:::://:/::///:::::--.`   ' + '\n'
    fausto += '           -:://:::://+++///+++++ooo//::::::--`    ' + '\n'
    fausto += '            .:::::::::::/osyhhyys+/////:::::-`     ' + '\n'
    fausto += '              `-::::::::::::----:::////////:`      ' + '\n'
    fausto += '                `.-://::://////////++ooo++-`       ' + '\n'
    fausto += '                    `-:/+/++++ooossssss/-`         ' + '\n'
    fausto += '                       `-:/+ooosssso/-             '
    return fausto


if __name__ == '__main__':
    stdin_input = ''
    for line in sys.stdin:
        stdin_input += line

    print(generate_message_balloon(stdin_input.strip('\n'), 30))
    print(faustao())
