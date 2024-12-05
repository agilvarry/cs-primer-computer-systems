section .text
global index
index:
	imul ecx, edx
	add ecx, r8d
	imul ecx, 4
	add rcx, rdi
	mov eax, [rcx]
	; rdi: matrix
	; esi: rows
	; edx: cols
	; ecx: rindex
	; r8d: cindex
	ret
