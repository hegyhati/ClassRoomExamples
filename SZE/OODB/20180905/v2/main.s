	.file	"main.cpp"
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
.LC7:
	.string	"Length: "
.LC8:
	.string	"AVG Speed: "
	.text
	.globl	main
	.type	main, @function
main:
.LFB1383:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	addq	$-128, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movq	$0, -104(%rbp)
	movsd	.LC0(%rip), %xmm0
	movsd	%xmm0, -96(%rbp)
	movsd	.LC0(%rip), %xmm0
	movsd	%xmm0, -88(%rbp)
	pxor	%xmm0, %xmm0
	movsd	%xmm0, -80(%rbp)
	leaq	-104(%rbp), %rax
	subq	$8, %rsp
	pushq	-80(%rbp)
	pushq	-88(%rbp)
	pushq	-96(%rbp)
	movq	%rax, %rdi
	call	_Z6appendRP6PLItem5Point
	addq	$32, %rsp
	movsd	.LC2(%rip), %xmm0
	movsd	%xmm0, -64(%rbp)
	movsd	.LC3(%rip), %xmm0
	movsd	%xmm0, -56(%rbp)
	movsd	.LC4(%rip), %xmm0
	movsd	%xmm0, -48(%rbp)
	leaq	-104(%rbp), %rax
	subq	$8, %rsp
	pushq	-48(%rbp)
	pushq	-56(%rbp)
	pushq	-64(%rbp)
	movq	%rax, %rdi
	call	_Z6appendRP6PLItem5Point
	addq	$32, %rsp
	movsd	.LC5(%rip), %xmm0
	movsd	%xmm0, -32(%rbp)
	movsd	.LC3(%rip), %xmm0
	movsd	%xmm0, -24(%rbp)
	movsd	.LC6(%rip), %xmm0
	movsd	%xmm0, -16(%rbp)
	leaq	-104(%rbp), %rax
	subq	$8, %rsp
	pushq	-16(%rbp)
	pushq	-24(%rbp)
	pushq	-32(%rbp)
	movq	%rax, %rdi
	call	_Z6appendRP6PLItem5Point
	addq	$32, %rsp
	movq	-104(%rbp), %rax
	movq	%rax, %rdi
	call	_Z5printP6PLItem
	movq	-104(%rbp), %rax
	movq	%rax, %rdi
	call	_Z6lengthP6PLItem
	movsd	%xmm0, -120(%rbp)
	movl	$.LC7, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	-120(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movq	%rax, %rdi
	call	_ZNSolsEPFRSoS_E
	movq	-104(%rbp), %rax
	movq	%rax, %rdi
	call	_Z8avgspeedP6PLItem
	movsd	%xmm0, -120(%rbp)
	movl	$.LC8, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movsd	-120(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movq	%rax, %rdi
	call	_ZNSolsEPFRSoS_E
	leaq	-104(%rbp), %rax
	movq	%rax, %rdi
	call	_Z5resetRP6PLItem
	movl	$0, %eax
	movq	-8(%rbp), %rdx
	xorq	%fs:40, %rdx
	je	.L3
	call	__stack_chk_fail
.L3:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1383:
	.size	main, .-main
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1573:
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
	jne	.L6
	cmpl	$65535, -8(%rbp)
	jne	.L6
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
.L6:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1573:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB1574:
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
.LFE1574:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_main
	.section	.rodata
	.align 8
.LC0:
	.long	0
	.long	1072693248
	.align 8
.LC2:
	.long	0
	.long	1074790400
	.align 8
.LC3:
	.long	0
	.long	1075052544
	.align 8
.LC4:
	.long	0
	.long	1077805056
	.align 8
.LC5:
	.long	0
	.long	1075314688
	.align 8
.LC6:
	.long	0
	.long	1078198272
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
