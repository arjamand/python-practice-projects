# 2022-10-24 19:00:57

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text,shift,direction):
    text_=[]
    code=[]
    if shift >26 :
        if shift%26!=0:
            shift=(shift%26)

    for x in text:
        # text_+=x
            
        if x in alphabet:
            indexes = [index for index in range(len(alphabet)) if alphabet[index] == (x)]
            z=0
            y = int(indexes[0+z])
            z+=1
            if direction=="encode":
                code.append("encoded")
                text_.append((alphabet[((y)+shift)]))
            elif direction=="decode":
                code.append("decoded")
                text_.append((alphabet[((y)-shift)]))
        else :
            text_.append(x)
    text__="".join(text_)
    print(f"The {code[0]} text is {text__} (Shift : {shift}).")
ceaser(text=text, shift=shift, direction=direction)

signal=True
while signal==True:

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt and 'e' to exit:\n")
    if direction=="encode" or direction=="decode" :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(text=text, shift=shift,direction=direction)
    elif direction=="e":
        signal=False
        print("\nGoodBye\n")
        exit()
