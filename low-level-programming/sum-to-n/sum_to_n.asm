section .text
global sum_to_n
sum_to_n:
	mov rax, 0
add_n:
	add rax, rdi
	sub rdi, 1
	cmp rdi
	jne add_n
	ret