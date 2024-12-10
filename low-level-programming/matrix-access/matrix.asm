section .text
global index
index:
	; rdi: matrix
	; esi: rows
	; edx: cols
	; ecx: rindex
	; r8d: cindex
	imul ecx, edx
	add ecx, r8d
	; imul ecx, 4
	; add rcx, rdi
	mov rax, [rdi + 4 *rcx]
    ret
