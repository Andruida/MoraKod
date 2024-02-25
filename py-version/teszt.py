import kodolo
from bitarray import bitarray
from bitarray import util as bitarrayutil
from random import randint

segment_eltort_bit: int = 0

def torik_e(esely: int) -> bool:
    torik: int = 1 + randint(0, 100)
    return torik < esely

def toro(data: bitarray, meret: int, honnan: int):
    global segment_eltort_bit
    if not isinstance(data, bitarray) or len(data) != 256:
        raise ValueError("Input bitarray must be 256 bits long, got " + str(len(data)))
    
    if honnan > 256 - meret:
        raise ValueError("Túl nagy a honnan!")
    
    lepes: int = 20 / meret
    esely: int = 30
    
    for i in range(meret*2+1):
        if torik_e(esely):
            data[honnan+i] = 1 - data[honnan+i]
            segment_eltort_bit += 1
            
    if i < meret:
        esely += lepes
    elif i >= meret: 
        esely -= lepes
        
    return data

if __name__ == "__main__":
    bitarray_list: list[bitarray] = []

    f = open("../bitek.txt", "r")
    
    for line in f:
        bitarray_list.append(bitarray(line[::-1]))
        
    for i in range(7, 20):
        nem_tort: int = 0
        osszes: int = 0
        eredmeny: float = 0
        toresi_esely: float = 0
        for bevitel in bitarray_list:
            forditott = kodolo.encode(bevitel)
            toro(forditott, i, 7)
            kiadas = kodolo.decode(forditott)
            
            if bevitel == kiadas:
                nem_tort += 1
            osszes += 1
        print(f"{i*2+1} méretű parabola zaj mintázása esetén:")
        eredmeny =  (nem_tort*100)/osszes
        print(f"{nem_tort} lett jó")
        print(f"{eredmeny}% lett jó a(z) {osszes} esetből.")
        print(f"{segment_eltort_bit} bit tört el a(z) {osszes*144} bitből.\n")
        segment_eltort_bit = 0


            