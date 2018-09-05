	.file	"PLItem.cpp"
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.text
	.globl	_Z6appendRP6PLItem5Point
	.type	_Z6appendRP6PLItem5Point, @function
_Z6appendRP6PLItem5Point:
.LFB1383:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	movq	-24(%rbp), %rax
	movq	(%rax), %rax
	testq	%rax, %rax
	jne	.L2
	movl	$32, %edi
	call	_Znwm
	movq	%rax, %rdx
	movq	-24(%rbp), %rax
	movq	%rdx, (%rax)
	movq	-24(%rbp), %rax
	movq	(%rax), %rax
	movq	16(%rbp), %rdx
	movq	%rdx, (%rax)
	movq	24(%rbp), %rdx
	movq	%rdx, 8(%rax)
	movq	32(%rbp), %rdx
	movq	%rdx, 16(%rax)
	movq	-24(%rbp), %rax
	movq	(%rax), %rax
	movq	$0, 24(%rax)
	jmp	.L6
.L2:
	movq	-24(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, -8(%rbp)
.L5:
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	testq	%rax, %rax
	je	.L4
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	movq	%rax, -8(%rbp)
	jmp	.L5
.L4:
	movl	$32, %edi
	call	_Znwm
	movq	%rax, %rdx
	movq	-8(%rbp), %rax
	movq	%rdx, 24(%rax)
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	movq	16(%rbp), %rdx
	movq	%rdx, (%rax)
	movq	24(%rbp), %rdx
	movq	%rdx, 8(%rax)
	movq	32(%rbp), %rdx
	movq	%rdx, 16(%rax)
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	movq	$0, 24(%rax)
.L6:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1383:
	.size	_Z6appendRP6PLItem5Point, .-_Z6appendRP6PLItem5Point
	.section	.rodata
.LC0:
	.string	"("
.LC1:
	.string	","
.LC2:
	.string	")["
.LC3:
	.string	"] -> "
	.text
	.globl	_Z5printP6PLItem
	.type	_Z5printP6PLItem, @function
_Z5printP6PLItem:
.LFB1384:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%r13
	pushq	%r12
	pushq	%rbx
	subq	$40, %rsp
	.cfi_offset 13, -24
	.cfi_offset 12, -32
	.cfi_offset 3, -40
	movq	%rdi, -56(%rbp)
	movq	-56(%rbp), %rax
	movq	%rax, -40(%rbp)
.L9:
	cmpq	$0, -40(%rbp)
	je	.L8
	movq	-40(%rbp), %rax
	movq	16(%rax), %rbx
	movq	-40(%rbp), %rax
	movq	8(%rax), %r12
	movq	-40(%rbp), %rax
	movq	(%rax), %r13
	movl	$.LC0, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%r13, -64(%rbp)
	movsd	-64(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$.LC1, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%r12, -64(%rbp)
	movsd	-64(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$.LC2, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rbx, -64(%rbp)
	movsd	-64(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$.LC3, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	-40(%rbp), %rax
	movq	24(%rax), %rax
	movq	%rax, -40(%rbp)
	jmp	.L9
.L8:
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEPFRSoS_E
	nop
	addq	$40, %rsp
	popq	%rbx
	popq	%r12
	popq	%r13
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1384:
	.size	_Z5printP6PLItem, .-_Z5printP6PLItem
	.globl	_Z5resetRP6PLItem
	.type	_Z5resetRP6PLItem, @function
_Z5resetRP6PLItem:
.LFB1385:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	testq	%rax, %rax
	je	.L12
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	addq	$24, %rax
	movq	%rax, %rdi
	call	_Z5resetRP6PLItem
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	_ZdlPv
	movq	-8(%rbp), %rax
	movq	$0, (%rax)
.L12:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1385:
	.size	_Z5resetRP6PLItem, .-_Z5resetRP6PLItem
	.globl	_Z6lengthP6PLItem
	.type	_Z6lengthP6PLItem, @function
_Z6lengthP6PLItem:
.LFB1386:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	cmpq	$0, -24(%rbp)
	je	.L14
	movq	-24(%rbp), %rax
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L15
.L14:
	pxor	%xmm0, %xmm0
	jmp	.L16
.L15:
	pxor	%xmm0, %xmm0
	movsd	%xmm0, -16(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -8(%rbp)
.L18:
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	testq	%rax, %rax
	je	.L17
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	pushq	16(%rax)
	pushq	8(%rax)
	pushq	(%rax)
	movq	-8(%rbp), %rax
	pushq	16(%rax)
	pushq	8(%rax)
	pushq	(%rax)
	call	_Z8distance5PointS_
	addq	$48, %rsp
	movapd	%xmm0, %xmm1
	movsd	-16(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, -16(%rbp)
	movq	-8(%rbp), %rax
	movq	24(%rax), %rax
	movq	%rax, -8(%rbp)
	jmp	.L18
.L17:
	movsd	-16(%rbp), %xmm0
.L16:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1386:
	.size	_Z6lengthP6PLItem, .-_Z6lengthP6PLItem
	.globl	_Z8avgspeedP6PLItem
	.type	_Z8avgspeedP6PLItem, @function
_Z8avgspeedP6PLItem:
.LFB1387:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%rdi, -40(%rbp)
	cmpq	$0, -40(%rbp)
	je	.L20
	movq	-40(%rbp), %rax
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L21
.L20:
	movsd	.LC5(%rip), %xmm0
	jmp	.L22
.L21:
	movq	-40(%rbp), %rax
	movsd	16(%rax), %xmm0
	movsd	%xmm0, -8(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, -16(%rbp)
.L24:
	cmpq	$0, -16(%rbp)
	je	.L23
	movq	-16(%rbp), %rax
	movsd	16(%rax), %xmm0
	movsd	%xmm0, -24(%rbp)
	movq	-16(%rbp), %rax
	movq	24(%rax), %rax
	movq	%rax, -16(%rbp)
	jmp	.L24
.L23:
	movq	-40(%rbp), %rax
	movq	%rax, %rdi
	call	_Z6lengthP6PLItem
	movapd	%xmm0, %xmm1
	movsd	-24(%rbp), %xmm0
	subsd	-8(%rbp), %xmm0
	divsd	%xmm0, %xmm1
	movapd	%xmm1, %xmm0
.L22:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1387:
	.size	_Z8avgspeedP6PLItem, .-_Z8avgspeedP6PLItem
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1577:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	cmpl	$1, -4(%rbp)
	jne	.L27
	cmpl	$65535, -8(%rbp)
	jne	.L27
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
.L27:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1577:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I__Z6appendRP6PLItem5Point, @function
_GLOBAL__sub_I__Z6appendRP6PLItem5Point:
.LFB1578:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1578:
	.size	_GLOBAL__sub_I__Z6appendRP6PLItem5Point, .-_GLOBAL__sub_I__Z6appendRP6PLItem5Point
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z6appendRP6PLItem5Point
	.section	.rodata
	.align 8
.LC5:
	.long	0
	.long	-1074790400
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
