with open('input2.txt', 'r') as infile:
    content = infile.read().splitlines()
    replace_dict = {}
    replace_list = []
    #NAMTAB
    for line in content:
        if 'MACRO' in line:
            start = content.index(line)
            line_parse = line.split()
            macro_name = line_parse[0]
            namtab_p1 = macro_name
            namtab_p2 = line_parse[len(line_parse)-1]
            arg = namtab_p2.split(',')
            c = 1
            for i in arg:
                replace_dict.setdefault(i, '?{}'.format(c))
                replace_list.append(i)
                c+=1
            with open('NAMTAB.txt', 'w') as outfile:
                outfile.write('{}\t{}\t{}\t{}'.format(macro_name, namtab_p1, namtab_p2, 'MEND'))
                pass
        if 'MEND' in line:
            end = content.index(line)
        else:
            pass
    #ARGTAB
    for line in content:
        if macro_name in line and 'MACRO' not in line:
            line_parse = line.split()
            arg_list = line_parse[len(line_parse)-1].split(',')
            with open('ARGTAB.txt', 'a') as outfile:
                for i in arg_list:
                    outfile.write('{}\n'.format(i))
        else:
            pass
    #DEFTAB
    for i in range(start, end+1):
        tmp = content[i].split()
        print(tmp)
        if 'MACRO' in tmp:
            content[i] = '{}\t{}'.format(tmp[0], tmp[len(tmp)-1])
        else:
            content[i] = content[i].lstrip()#對齊用
            for t in replace_list:
                find_result = tmp[len(tmp)-1].find(t)
                if find_result != -1:#!= -1 >>> has to be replaced
                    #print(content[i])
                    content[i] = content[i].replace(t, replace_dict[t])
        with open('DEFTAB.txt', 'a') as outfile:
            outfile.write('{}\n'.format(content[i]))
    print('----------------------------')
    print(replace_dict)
    print(replace_list)