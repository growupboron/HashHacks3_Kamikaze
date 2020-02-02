braille = {
   '!': '001110',
   '?': '001011',
   '.': '001101',
   ';': '001010',
   ':': '001100',
   '-': '000011',
   ',': '001000',
   "’": '000010',
   '"': '000100',
   ' ': '000000',
   'a': '100000',
   'b': '101000',
   'c': '110000',
   'd': '110100',
   'e': '100100',
   'f': '111000',
   'g': '111100',
   'h': '101100',
   'i': '011000',
   'j': '011100',
   'k': '100010',
   'l': '101010',
   'm': '110010',
   'n': '110110',
   'o': '100110',
   'p': '111010',
   'q': '111110',
   'r': '101110',
   's': '011010',
   't': '011110',
   'u': '100011',
   'v': '101011',
   'w': '011101',
   'x': '110011',
   'y': '110111',
   'z': '100111',
   '1': '100000',
   '2': '101000',
   '3': '110000',
   '4': '110100',
   '5': '100100',
   '6': '111000',
   '7': '111100',
   '8': '101100',
   '9': '011000',
   '0': '011100',
   '#':'010111',
   
}
text_file = open("camera200.txt", "r")
lines = text_file.read().split()
print(lines)

#print (len(lines))
mystr=''
lines=[s.replace('\n', mystr) for s in lines]
#print (lines)
i=0
a=[]
while(i<len(lines)):
    len1=len(lines[i])
    j=0
    while(j<len1):
        ch=lines[i][j]
        ch=str.lower(ch)
        if(ch!='('and ch!=')'and ch!='‘'and ch!='|'and ch!='”'and ch!='“'and ch!='«'):
            a.append(list(map(int,braille[str(ch)])))    
        if(ch.isnumeric()):
            a.append(list(map(int,braille['#'])))
            a.append(list(map(int,braille[str(ch)])))            
        j=j+1
    i=i+1
print(a)



#print (len(lines))



