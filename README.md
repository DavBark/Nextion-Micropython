# Nextion-Micropython
Repository für die Verwendung eins Nextion HMI Displays mit einem ESP32

![Nextion Display](Bilder/NX3224F028.jpg)

# Links

[Quickstart](https://itead.cc/nextion-display/)

[Nextion Software](https://nextion.tech/nextion-editor/#_section1)

[Software Tutorials](https://www.boecker-systemelektronik.de/Seite-/-Kategorie-1/NextionTutorials/Der-Nextion-Editor)

[UART Micropython](https://docs.micropython.org/en/latest/library/machine.UART.html)

## Anschluss Programieren (PC -> Nextion)
#
| USB zu TTL | Nextion |
| ------------------ | ------------------ |
| 5V | Red (5V) |
| GND | Black (GND) |
| RX | Blue (TX) |
| TX | Yellow (RX) |


## Kommunikation

Anschluss von ESP zum Display
| ESP | Nextion |
| ------------ | ----------- |
| 5V | Red (5V) |
| GND | Black (GND) |
| RX (Pin 26) | Blue (TX) |
| TX (Pin 25) | Yellow (RX) |

Die Kommunikation von ESP und Nextion geschieht über UART.
```python
import machine
uart = machine.UART(1, tx=25, rx=26, baudrate=9600)
```
## Senden von Befehlen
```python
end_cmd = b'\xFF\xFF\xFF'

def send(cmd):
    uart.write(cmd)
    uart.write(end_cmd)
    time.sleep_ms(100)
    answerNex =  uart.read()
    print("Response:", answerNex)
    return answerNex
```


## Übersicht an Befehlen
[Weitere Befehle](https://www.boecker-systemelektronik.de/Seite-/-Kategorie-1/NextionTutorials/Befehlsuebersicht)

## Beispiel Befehle
Die Seite kann auch in der Nextion-Software bennant werden
```python
# Wechsel zur Seite 1
send("page 1")

# Was auch möglich ist:
send("page Hauptseite")
```
Lesen, was im Textbaustein t1 steht
```python
send("get t1.txt")
```
Welchen Wert hat der Baustein n0 
```python
send("get n0.val")
```
