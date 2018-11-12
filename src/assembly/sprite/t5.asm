org 32768
PUSH HL
LD A, 2
LD BC, 255
OUT (C), A
LD B, 8
LD IX, sprite
LD HL, 16384

LD DE, 24576
lp1 LD A, (IX)
LD (HL), A
LD A, (IX+1)
LD E, H
LD H, D
LD (HL), A
INC IX
INC IX
LD H, E
INC D
INC H
DJNZ lp1
POP HL
XOR A
wk IN A,(254)
AND 31
CP 31
JR Z, wk
XOR A
LD BC, 255
OUT (C),A
RET

sprite DB 60,  6
DB 126, 6
DB 124, 126
DB 240, 71
DB 240, 71
DB 124, 126
DB 126, 6
DB 60, 6

end 32768