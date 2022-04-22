def auswertenZahl(cmd):
    zahl = nextion_cmd(cmd)
    time.sleep_ms(100)
    zahl = zahl.replace(b'\xff\xff\xff', b'')
    zahl = zahl.replace(b'p', b'')
    zahl = zahl.decode("utf-8")
    return int(zahl)

def auswertenBuchstaben(cmd):
    buchstaben = nextion_cmd(cmd)
    #print(buchstaben)
    time.sleep_ms(100)
    buchstaben = buchstaben.replace(b'\xff\xff\xff', b'')
    buchstaben = buchstaben.replace(b'p', b'')
    buchstaben = buchstaben.decode("utf-8")
    return buchstaben
