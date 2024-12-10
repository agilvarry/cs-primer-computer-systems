section .text
global pangram
pangram:
	mov rcx, 0	
.loop:
	movzx edx, byte [rdi] ; c = *s
	cmp edx, 0 ; (c = *s) 
	je .done ; != '\0'
	inc rdi ; *s++
	cmp edx, '@'
	jl .loop ; (c < '@') continue
	bts ecx, edx ;bs |= 1 << (c & 0x1f)
	jmp .loop
.done:
	mov eax, 0
	and ecx, 0x07fffffe
	cmp ecx, 0x07fffffe
	je .equal
	ret
.equal:
	mov eax, 1