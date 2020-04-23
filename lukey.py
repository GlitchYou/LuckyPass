#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def randkey(mn=8, mx=8, keys=1000, wor='1234567890', msk='{w}'):
    """
    --> Sorteia senhas aleatorias
    :param mn:		minimo de largura de caracteres     (Padrão:    8...)
    :param mx:		maximo de largura de caravteres     (Padrão:    8...)
    :param keys:	quantidade de sehnas geradas        (Padrão: 1000...)
    :param wor:		lista de palavras aleatórias        (Padrão:  123...)
    :param msk:		prefixo de palavras aeatórias       (Padrão:  {w}...)
                        {w} -> lista de palavras em wor     [ABCABC123:<>...]
                        {l} -> lista do alfabeto minusculo  [abcdefghijkj...]
                        {u} -> lista do alfabeto maiusculo  [ABCDEFGHIJKJ...]
                        {d} -> lista de números             [0123456789  ...]
    """

    from random import choice, randint

    low = 'abcdefghijklmnopqrstuvwxyz'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '1234567890'

    for process in range(0, keys):
        w = l = u = d = ''
        rand = randint(mn, mx)
        for val in range(0, rand):
            w += choice(wor)

            l += choice(low)
            u += choice(upp)
            d += choice(dig)

        print(eval(f"f'{msk}'"))


def shargs(function, *types):
    """
    --> Facilita o processo de envio dos parâmetros entre o terminal
    e a função desejada.

    $ file.py [ --help | -h ] mostra o help com edições

    :param function: função que deseja passar os parâmetros pelo terminal
    :param types: força a entrada de tipos expecificos no parâmetros
    :return: None

    Exemplos:

    def sua_função(a, b, c):
        print(a, b, c)

    shargs(sua_função)

    $ ./file.py 8 texto --c 0
    > 8 texto 0

    ------------------------------------

    def sua_fução(a, b, c=9):
        print(a, b, a + c)

    shargs(sua_função, int, str)

    $ python3 file.py 5 6 7
    > 5 6 16

    ------------------------------------

    def sua_função(a :int, b: int, c: int):
        print(a - b, b + c, c * a)

    shargs(sua_função)

    $ ./file.py --b  5 --a 2 --c 3
    > 3 8 6

    -------------------------------------

    def sua_função(a=0, b=1, c=2):
        print(a, b, c)

    shargs(sua_função)
    $ ./file.py
    > 0 1 2

    --------------------------------------
    """
    from inspect import signature, getsource
    from re import findall, sub, S
    from sys import argv as args

    # Remover argumentos inutilisados
    if '.py' in args[0]:
        del args[0]
    else:
        del args[0]
        del args[0]

    # Obter informações da função
    name = function.__name__
    filename = function.__code__.co_filename
    source = getsource(function)

    # Obter códigos acima da função
    script = open(filename, 'rt', encoding='=utf-8').read()
    script = findall(fr'(.+)def {name}\(.+?\):', script, S)[0]

    # Obter parâmetros
    parans = signature(function)
    parans = parans.parameters.items()
    parans = dict(parans)

    # Obter objeto da classe
    re_cls = r"<class '(.+?)'>"

    run = ''

    # Ajuda
    if len(args) > 0:

        # Ajuda Adicional
        if args[0] in ['-h', '--help']:
            helper = f'{"":4}--> Parâmetros para o terminal:\n'
            for k in parans:
                helper += f'{"":10}--{k:10}<==>     {parans[k]}\n'

            helper += f'\n{"":10}{"[-h|--help]":10} <==>     Mostra o help com edições\n'

            source = sub(fr'(def {name}\(.+?\):\n.+)', fr'\1\n{helper}', source)

            # Executa o help
            exec(f'{source}\nhelp({name})')
            exit()

    # Substirtuir parâmetros por tipo
    for i, k in enumerate(parans):

        # Se o tipo contém no types: pula
        if i < len(types):
            parans[k] = types[i]
            continue

        v = parans[k]
        v = sub(fr'{k}|(:|=)\s?', r'', str(v))

        # Testa se existe um objeto em str
        if_cls = len(findall(re_cls, v)) > 0

        # Adapta os tipos
        if if_cls:
            v = sub(re_cls, r'\1', v)
            v = eval(v)

        elif v == '*':
            del parans[k]
        else:
            try:
                v = type(eval(v))
            except:
                v = type(v)

        parans[k] = v

    # Separar chaves e valores
    keys = list(parans.keys())
    vals = list(parans.values())

    run_args = []

    # Separar param e param=valor
    for i, a in enumerate(args):

        # param=valor
        if a[2:] in keys and a[:2] == '--':
            ik = keys.index(a[2:])

            try:
                v = vals[ik]
                val = f"'{args[i + 1]}'" if v == str else args[i + 1]
            except:
                val = f"'{args[i + 1]}'"

            run_args.append(f'{a[2:]}={val}')
            del args[i]

        # param
        else:

            try:
                val = f"'{a}'" if vals[i] == str else a
            except:
                val = f"'{a}'"

            run += f'{val}, '

    # Adcionar ao final param=valo
    for val in run_args:
        run += f'{val}, '

    # Adaptar Resultados
    run = run[:-2]

    # Executar
    try:
        exec(f'{script}\n{source}\n{name}({run})')

    # Ocorrer um erro motra a função executada e a causa do erro
    except Exception as error:
        print(f'\33[31;4m'
              f'Erro ao executar: {name}({run})\n'
              f'Causa: {error.args}\n'
              f'\033[m')


shargs(randkey)

