default rel

section .text
	pi DD 3.1415926535
	x DD 1.0
	y DD 3.0
global volume

volume:
	movss xmm2, [x]
	movss xmm3, [y]
	divss xmm2, xmm3 ;(1/3)
	mulss xmm2, [pi] ;(1/3) * pi
	mulss xmm0, xmm0 ; r^2
	mulss xmm0, xmm2 ;(1/3) * pi * r^2
	mulss xmm0, xmm1 ;(1/3) * pi * r^2 *h
 	ret
