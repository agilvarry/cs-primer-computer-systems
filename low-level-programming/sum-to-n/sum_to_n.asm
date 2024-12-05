; section .text
; global sum_to_n
; sum_to_n:
;     mov rax, 0
; add_n:
;     add rax, rdi
;     sub rdi, 1
;     cmp rdi, 0
;     jge add_n
;     ret 


section .text
global sum_to_n
sum_to_n:
	mov eax, edi
	add edi, 1
	imul eax, edi
	shr eax, 1
	ret
