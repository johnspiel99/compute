def gues():
    secret_word = 'shit'
    gues = ''
    while gues != secret_word:
        gues = input('enter gues: ')
        if gues == secret_word:
            print('game win')
        else:
            print('game lose')

gues()
