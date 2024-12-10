section .text
global pangram
pangram:
	; rdi: source string
	;; rdx address
	;sal - shift
	;or - or
	mov eax, 0
	mov ecx, 0x07fffffe

	ret
