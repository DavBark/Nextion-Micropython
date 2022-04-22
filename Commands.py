# Beispiel: print(senden("get t1.txt"))
# >>> b'pHallo\xff\xff\xff'
def senden(cmd):
    uart.write(cmd)
    uart.write(end_cmd)
    time.sleep_ms(100)
    answerNex =  uart.read()
    #print("Response:", answerNex) # Uncommend for Deebugging
    return answerNex

# Beispiel: print(auswertenBuchstaben("get n1.val"))
# >>> 50
def auswertenZahl(cmd):
    zahl = nextion_cmd(cmd)
    time.sleep_ms(100)
    zahl = zahl.replace(b'\xff\xff\xff', b'')
    zahl = zahl.replace(b'p', b'')
    zahl = zahl.decode("utf-8")
    return int(zahl)


# Beispiel: print(auswertenBuchstaben("get t1.txt"))
# >>> 'Hallo'
def auswertenBuchstaben(cmd):
    buchstaben = nextion_cmd(cmd)
    time.sleep_ms(100)
    buchstaben = buchstaben.replace(b'\xff\xff\xff', b'')
    buchstaben = buchstaben.replace(b'p', b'')
    buchstaben = buchstaben.decode("utf-8")
    return buchstaben