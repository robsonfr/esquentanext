org 32768
	ld a,2
	ld bc,255
	out (c),a

	push hl

	ld hl, imagem
	ld de, 16384
	ld bc, 6144
	ldir

	ld hl, imagem
	ld de, 6144
	add hl, de
	ld de, 24576
	ld bc, 6144
	ldir

	call wk
	ld a,0
	ld bc,255
	out (c),a
	call wk
	
	pop hl
	ret

wk	ld hl, 23560
	ld (hl), 0
c1	ld a, (hl)
	cp 0
	jr z, c1
	ret

imagem incbin "emoji6.scr"
end 32768