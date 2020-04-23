# LuckyPass
Teste sua sorte ao crakear um handshake WPA2 com um comando feito em python3 + aircrack-ng com uma simples automação
para obter as redes dentro do handshake.cap para tentar descobrir uma senha na sorte com senhas ou palavras chaves
aleatórias.

## Uso

    ./main.py 1 --wor 123abc --msk test-{w} handshake
    
 ### Parâmetros

* --mn = 8
* --mx = 8
* --keys = 1000
* --wor = '1234567890'
* -- msk = '{w}'
