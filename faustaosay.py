#!/usr/bin/env python3
import sys


def balao(s, l):
    bal = ''
    bal += '  ' + '_'*l + '\n'
    if len(s) <= l:
        bal += '< ' + s.ljust(l) + ' >' + '\n'
    else:
        i = 0
        while True:
            line = s[i*l:(i*l)+l]
            if i == 0:
                bal += '/ ' + line.ljust(l) + ' \\' + '\n'
            elif len(line) < l:
                bal += '\\ ' + line.ljust(l) + ' /' + '\n'
                break
            else:
                bal += '| ' + line.ljust(l) + ' |' + '\n'
            i += 1
    bal += '  ' + '-'*l + '\n'
    bal += ' '*9 + '\\' + '\n'
    bal += ' '*10 + '\\'
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
    s = ''
    for line in sys.stdin:
        s += line

    print(balao(s.strip('\n'), 30))
    print(faustao())
