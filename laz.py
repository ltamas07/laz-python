fi = open('laz.txt','w')

nevek = []
hőmérséklet = []
for i in range(3):
    név = input('Add meg a neved: ')
    hő = float(input('Add meg a testhőmérsékleted: '))
    hőmérséklet.append(hő)
    nevek.append(név)
    # print(nevek)
    # print(hőmérséklet)
    if hő > 38:
        print(név, 'Lázas.')
        fi.write(f'{név} Lázas.\n')
    elif 37 < hő < 38:
        print(név,'-nak Hőemelkedése van.')
        fi.write(f'{név}-nak Hőemelkedése van.\n')
    else:
        print(név, 'Nem lázas.')
        fi.write(f'{név} Nem lázas.\n')

fi.close()