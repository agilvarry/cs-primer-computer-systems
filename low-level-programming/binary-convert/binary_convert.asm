section .text
global binary_convert
binary_convert:
	xor eax, eax
.loop:
	movzx edx, byte [rdi] ; c = *s
	inc rdi
	cmp edx, 0
	je .done
	shl eax, 1
	and edx, 1
	or eax, edx
	jmp .loop
.done:
	ret
