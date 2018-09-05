	.file	"Point.cpp"
	.text
	.globl	_Z8distance5PointS_
	.type	_Z8distance5PointS_, @function
_Z8distance5PointS_:
.LFB222:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movsd	16(%rbp), %xmm0
	movsd	40(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movapd	%xmm0, %xmm1
	movsd	16(%rbp), %xmm0
	movsd	40(%rbp), %xmm2
	subsd	%xmm2, %xmm0
	mulsd	%xmm0, %xmm1
	movsd	24(%rbp), %xmm0
	movsd	48(%rbp), %xmm2
	subsd	%xmm2, %xmm0
	movapd	%xmm0, %xmm2
	movsd	24(%rbp), %xmm0
	movsd	48(%rbp), %xmm3
	subsd	%xmm3, %xmm0
	mulsd	%xmm2, %xmm0
	addsd	%xmm1, %xmm0
	call	sqrt
	movq	%xmm0, %rax
	movq	%rax, -8(%rbp)
	movsd	-8(%rbp), %xmm0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE222:
	.size	_Z8distance5PointS_, .-_Z8distance5PointS_
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
