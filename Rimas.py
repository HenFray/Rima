import queue


PrimeraPalabra = input("Primera palabra: ")
SegundaPalabra = input("SegundaPalabra: ")

if len(PrimeraPalabra)<3 or len(SegundaPalabra)<3: #la primera palabra tiene mas de 3 caracteres ?
    print("No rima por que tiene menos de 3 caracteres")
elif PrimeraPalabra[-3: ] == SegundaPalabra[-3: ]:
    print("Las palabras riman")
elif PrimeraPalabra[-2: ] == SegundaPalabra[-2: ]:
    print("las palabras riman")
else:
    print("Las palabras no riman")
