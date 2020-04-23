# LuckyPass
Teste sua sorte ao crakear um handshake WPA2 com um comando feito em python3 + aircrack-ng com uma simples automação
para obter as redes dentro do handshake.cap para tentar descobrir uma senha na sorte com senhas ou palavras chaves
aleatórias.

## Uso

    ./main.py 1 --wor 123abc --msk test-{w} handshake

  --mn Minimo               Padrão: 8
  --mx Maximo               Padrão: 8
  --keys Quantidade         Padrão: 1000
  --wor Lista-de-Palavras   Padrão: '1234567890'
  --msk Macara/Modelo       Padrão: '{w}'
