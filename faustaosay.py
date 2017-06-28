def f(s,l):
    print('  ' + '_'*l)
    if len(s) <= l:
            print('< ' + s.ljust(l) + ' >')
    else:
            lines = s.split()
            i = 0
            while True:
                    line = s[i*l:(i*l)+l]
                    if i == 0:
                            print('/ ' + line.ljust(l) + ' \\')
                    elif len(line) < l:
                            print('\\ ' + line.ljust(l) + ' /')
                            break
                    else:
                            print('| ' + line.ljust(l) + ' |')
                    i += 1
    print('  ' + '-'*l)