import unittest

import os
import find_slycot


class TestFindSlycotFindFunctionUsedFortran(unittest.TestCase):
    def setUp(self):
        self.result_dict = {os.path.join('..', '..', 'slycot', 'slycot', 'src'): {
            'SB04MD.f': [(196, "         CALL XERBLA( 'SB04MD', -INFO )"),
                         (222, '         CALL DSWAP( I-1, B(1,I), 1, B(I,1), LDB )'),
                         (230, "      CALL DGEES( 'Vectors', 'Not ordered', SELECT, M, B, LDB,"),
                         (242, '      CALL DGEHRD( N, ILO, IHI, A, LDA, DWORK(ITAU), DWORK(JWORK),'),
                         (251, "      CALL DORMHR( 'Left', 'Transpose', N, M, ILO, IHI, A, LDA,"),
                         (257, "         CALL DGEMM( 'No transpose', 'No transpose', N, M, M, ONE, C,"),
                         (259, "         CALL DLACPY( 'Full', N, M, DWORK(JWORK), N, C, LDC )"),
                         (264, "            CALL DGEMV( 'Transpose', M, M, ONE, Z, LDZ, C(I,1), LDC,"),
                         (266, '            CALL DCOPY( M, DWORK(JWORK), 1, C(I,1), LDC )'),
                         (282, '            CALL SB04MY( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (296, '            CALL SB04MU( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (312, '         CALL SB04MY( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (326, "      CALL DORMHR( 'Left', 'No transpose', N, M, ILO, IHI, A, LDA,"),
                         (332, "         CALL DGEMM( 'No transpose', 'Transpose', N, M, M, ONE, C, LDC,"),
                         (334, "         CALL DLACPY( 'Full', N, M, DWORK(JWORK), N, C, LDC )"),
                         (338, "            CALL DGEMV( 'No transpose', M, M, ONE, Z, LDZ, C(I,1), LDC,"),
                         (340, '            CALL DCOPY( M, DWORK(JWORK), 1, C(I,1), LDC )')],
            'TB04AD.f': [(320, "         CALL XERBLA( 'TB04AD', -INFO )"),
                         (339, '         CALL AB07MD( JOBD, N, M, P, A, LDA, B, LDB, C, LDC, D, LDD,'),
                         (346, "         CALL DLASET( 'Full', PWORK, MWORK, ZERO, ZERO, UCOEFF(1,1,K),"),
                         (353, '      CALL TB04AY( N, MWORK, PWORK, A, LDA, B, LDB, C, LDC, D, LDD,'),
                         (365, '         CALL TB01XD( JOBD, N, MWORK, PWORK, IWORK(1)+IWORK(2)-1, N-1,'),
                         (383, '                  CALL DSWAP( MPLIM-J, UCOEFF(J+1,J,K), 1,')],
            'SB02MT.f': [(339, "         CALL XERBLA( 'SB02MT', -INFO )"),
                         (378, '         CALL DCOPY( M, R, LDR+1, DWORK, 1 )'),
                         (382, '               CALL DCOPY( J-1, R(1,J), 1, R(J,1), LDR )'),
                         (388, '               CALL DCOPY( J-1, R(J,1), LDR, R(1,J), 1 )'),
                         (392, '         CALL DPOTRF( UPLO, M, R, LDR, INFO )'),
                         (398, '            CALL DPOCON( UPLO, M, R, LDR, RNORM, RCOND, DWORK, IWORK,'),
                         (415, '            CALL DCOPY( M, DWORK, 1, R, LDR+1 )'),
                         (419, '                  CALL DCOPY( J-1, R(J,1), LDR, R(1,J), 1 )'),
                         (425, '                  CALL DCOPY( J-1, R(1,J), 1, R(J,1), LDR )'),
                         (434, '            CALL DSYTRF( UPLO, M, R, LDR, IPIV, DWORK, LDWORK, INFO )'),
                         (445, '            CALL DSYCON( UPLO, M, R, LDR, IPIV, RNORM, RCOND, DWORK,'),
                         (470, "         CALL DTRSM( 'Right', UPLO, TRANS, 'Non-unit', N, M,"),
                         (477, "            CALL DSYRK( UPLO, 'No transpose', N, M, ONE, B, LDB, ZERO,"),
                         (487, "            CALL DTRSM( 'Right', UPLO, TRANS, 'Non-unit', N, M,"),
                         (492, "            CALL DGEMM( 'No transpose', 'Transpose', N, N, M, -ONE, B,"),
                         (497, "            CALL DSYRK( UPLO, 'No transpose', N, M, -ONE, L, LDL, ONE,"),
                         (508, '            CALL DCOPY( N, B(1,J), 1, DWORK(J), M )'),
                         (511, '         CALL DSYTRS( UPLO, M, N, R, LDR, IPIV, DWORK, M, INFO )'),
                         (521, "                  CALL DGEMV( 'No transpose', J, M, ONE, B, LDB,"),
                         (529, "                  CALL DGEMV( 'Transpose', M, J, ONE, DWORK, M, B(J,1),"),
                         (543, '               CALL DCOPY( N, L(1,J), 1, DWORK(J), M )'),
                         (546, '            CALL DSYTRS( UPLO, M, N, R, LDR, IPIV, DWORK, M, INFO )'),
                         (550, "            CALL DGEMM( 'No transpose', 'No transpose', N, N, M, -ONE,"),
                         (559, "                  CALL DGEMV( 'No transpose', J, M, -ONE, L, LDL,"),
                         (567, "                  CALL DGEMV( 'Transpose', M, J, -ONE, DWORK, M, L(J,1),")],
            'SG02AD.f': [(623, "         CALL XERBLA( 'SG02AD', -INFO )"),
                         (680, '         CALL DLASCL( QTYPE, 0, 0, SCALE, ONE, NP, N, Q, LDQ, INFO1 )'),
                         (681, '         CALL DLASCL( RTYPE, 0, 0, SCALE, ONE, MP, M, R, LDR, INFO1 )'),
                         (683, "     $      CALL DLASCL( 'G', 0, 0, SCALE, ONE, N, M, L, LDL, INFO1 )"),
                         (693, "      CALL SB02OY( 'Optimal control', DICO, JOBB, FACT, UPLO, JOBL,"),
                         (702, '         CALL DLASCL( QTYPE, 0, 0, ONE, SCALE, NP, N, Q, LDQ, INFO1 )'),
                         (703, '         CALL DLASCL( RTYPE, 0, 0, ONE, SCALE, MP, M, R, LDR, INFO1 )'),
                         (705, "     $      CALL DLASCL( 'G', 0, 0, ONE, SCALE, N, M, L, LDL, INFO1 )"),
                         (725, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OV, NN, T,"),
                         (728, '            CALL DSWAP( N, ALFAR(NP1), 1, ALFAR, 1 )'),
                         (729, '            CALL DSWAP( N, ALFAI(NP1), 1, ALFAI, 1 )'),
                         (730, '            CALL DSWAP( N, BETA (NP1), 1, BETA , 1 )'),
                         (732, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OV, NN, S,"),
                         (738, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OW, NN, S,"),
                         (742, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OU, NN, S,"),
                         (765, "      CALL DGEMM( 'No transpose', 'No transpose', N, N, N, ONE, E, LDE,"),
                         (767, "      CALL DLACPY( 'Full', N, N, X, LDX, U, LDU )"),
                         (768, '      CALL DGEQRF( NN, N, U, LDU, X, DWORK, LDWORK, INFO1 )'),
                         (770, '      CALL DORGQR( NN, N, N, U, LDU, X, DWORK, LDWORK, INFO1 )'),
                         (776, "      CALL DGEMM( 'Transpose', 'No transpose', N, N, N, ONE, U, LDU,"),
                         (811, '            CALL DSWAP( N-I, U(N+I,I+1), LDU, U(N+I+1,I), 1 )'),
                         (820, "         CALL MB02PD( 'Equilibrate', 'Transpose', N, N, U, LDU,"),
                         (829, '            CALL DSWAP( N-I, U(N+I,I+1), LDU, U(N+I+1,I), 1 )'),
                         (845, "               CALL MB01SD( 'Row scaling', N, N, U, LDU, DWORK(IWR),"),
                         (855, "               CALL MB01SD( 'Column scaling', NN, N, U, LDU, DWORK(IWR),"),
                         (874, "         CALL DLACPY( 'Full', N, N, U, LDU, S(NP1,1), LDS )"),
                         (875, "         CALL DLACPY( 'Full', N, N, U(NP1,1), LDU, X, LDX )"),
                         (879, "         CALL MB02VD( 'No Transpose', N, N, S(NP1,1), LDS, IWORK, X,"),
                         (895, "            CALL DGECON( '1-norm', N, S(NP1,1), LDS, UNORM, RCONDU,"),
                         (910, "      CALL DLASET( 'Full', N, N, ZERO, ZERO, S(NP1,1), LDS )"),
                         (915, '         CALL DAXPY( N-I, ONE, X(I,I+1), LDX, X(I+1,I), 1 )'),
                         (916, '         CALL DSCAL( N-I, HALF, X(I+1,I), 1 )'),
                         (917, '         CALL DCOPY( N-I, X(I+1,I), 1, X(I,I+1), LDX )'),
                         (924, "         CALL DLASCL( 'G', 0, 0, ONE, SCALE, N, N, X, LDX, INFO1 )")],
            'SB04QD.f': [(201, "         CALL XERBLA( 'SB04QD', -INFO )"),
                         (227, '         CALL DSWAP( I-1, B(1,I), 1, B(I,1), LDB )'),
                         (235, "      CALL DGEES( 'Vectors', 'Not ordered', SELECT, M, B, LDB,"),
                         (247, '      CALL DGEHRD( N, ILO, IHI, A, LDA, DWORK(ITAU), DWORK(JWORK),'),
                         (256, "      CALL DORMHR( 'Left', 'Transpose', N, M, ILO, IHI, A, LDA,"),
                         (266, "         CALL DGEMM( 'No transpose', 'No transpose', N, M, M, ONE, C,"),
                         (268, "         CALL DLACPY( 'Full', N, M, DWORK(JWORK), N, C, LDC )"),
                         (276, "            CALL DGEMM( 'NoTranspose', 'NoTranspose', BL, M, M, ONE,"),
                         (278, "            CALL DLACPY( 'Full', BL, M, DWORK(JWORK), BL, C(I,1), LDC )"),
                         (284, "            CALL DGEMV( 'Transpose', M, M, ONE, Z, LDZ, C(I,1), LDC,"),
                         (286, '            CALL DCOPY( M, DWORK(JWORK), 1, C(I,1), LDC )'),
                         (302, '            CALL SB04QY( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (315, '            CALL SB04QU( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (330, '         CALL SB04QY( M, N, IND, A, LDA, B, LDB, C, LDC,'),
                         (343, "      CALL DORMHR( 'Left', 'No transpose', N, M, ILO, IHI, A, LDA,"),
                         (349, "         CALL DGEMM( 'No transpose', 'Transpose', N, M, M, ONE, C, LDC,"),
                         (351, "         CALL DLACPY( 'Full', N, M, DWORK(JWORK), N, C, LDC )"),
                         (359, "            CALL DGEMM( 'NoTranspose', 'Transpose', BL, M, M, ONE,"),
                         (361, "            CALL DLACPY( 'Full', BL, M, DWORK(JWORK), BL, C(I,1), LDC )"),
                         (367, "            CALL DGEMV( 'No transpose', M, M, ONE, Z, LDZ, C(I,1), LDC,"),
                         (369, '            CALL DCOPY( M, DWORK(JWORK), 1, C(I,1), LDC )')],
            'SG03AD.f': [(459, "         CALL XERBLA( 'SG03AD', -INFO )"),
                         (494, "         CALL DGEGS( 'Vectors', 'Vectors', N, A, LDA, E, LDE, ALPHAR,"),
                         (518, "               CALL MB01RW( UPLO, 'Transpose', N, N, X, LDX, Q, LDQ,"),
                         (521, "               CALL MB01RW( UPLO, 'Transpose', N, N, X, LDX, Z, LDZ,"),
                         (526, "               CALL MB01RD( UPLO, 'Transpose', N, N, ZERO, ONE, X, LDX,"),
                         (529, "               CALL MB01RD( UPLO, 'Transpose', N, N, ZERO, ONE, X, LDX,"),
                         (535, '               CALL DCOPY( N-I, X(I+1,I), 1, X(I,I+1), LDX )'),
                         (543, '            CALL SG03AX( TRANS, N, A, LDA, E, LDE, X, LDX, SCALE, INFO1)'),
                         (547, '            CALL SG03AY( TRANS, N, A, LDA, E, LDE, X, LDX, SCALE, INFO1)'),
                         (562, "               CALL MB01RW( 'Upper', 'NoTranspose', N, N, X, LDX, Z,"),
                         (565, "               CALL MB01RW( 'Upper', 'NoTranspose', N, N, X, LDX, Q,"),
                         (570, "               CALL MB01RD( 'Upper', 'NoTranspose', N, N, ZERO, ONE, X,"),
                         (573, "               CALL MB01RD( 'Upper', 'NoTranspose', N, N, ZERO, ONE, X,"),
                         (578, '            CALL DCOPY( N-I, X(I,I+1), LDX, X(I+1,I), 1 )'),
                         (592, '         CALL DLACON( N*N, DWORK(N*N+1), DWORK, IWORK, EST, KASE )'),
                         (601, '               CALL SG03AX( ETRANS, N, A, LDA, E, LDE, DWORK, N, SCALE1,'),
                         (606, '               CALL SG03AY( ETRANS, N, A, LDA, E, LDE, DWORK, N, SCALE1,')],
            'SB03MD.f': [(421, "         CALL XERBLA( 'SB03MD', -INFO )"),
                         (448, "         CALL DGEES( 'Vectors', 'Not ordered', SELECT, N, A, LDA, SDIM,"),
                         (463, '         CALL MB01RD( UPLO, TRANST, N, N, ZERO, ONE, C, LDC, U, LDU, C,'),
                         (467, '            CALL DCOPY( I-1, C(1,I), 1, C(I,1), LDC )'),
                         (476, '            CALL SB03MY( TRANA, N, A, LDA, C, LDC, SCALE, INFO )'),
                         (478, '            CALL SB03MX( TRANA, N, A, LDA, C, LDC, SCALE, DWORK, INFO )'),
                         (486, '         CALL MB01RD( UPLO, NTRNST, N, N, ZERO, ONE, C, LDC, U, LDU, C,'),
                         (490, '            CALL DCOPY( I-1, C(1,I), 1, C(I,1), LDC )'),
                         (511, '         CALL DLACON( NN, DWORK(NN+1), DWORK, IWORK, EST, KASE )'),
                         (515, '                  CALL SB03MY( TRANA, N, A, LDA, DWORK, N, SCALEF,'),
                         (518, '                  CALL SB03MX( TRANA, N, A, LDA, DWORK, N, SCALEF,'),
                         (523, '                  CALL SB03MY( NOTRA, N, A, LDA, DWORK, N, SCALEF,'),
                         (526, '                  CALL SB03MX( NOTRA, N, A, LDA, DWORK, N, SCALEF,')],
            'TD04AD.f': [(329, "         CALL XERBLA( 'TD04AD', -INFO )"),
                         (349, "               CALL DLASET( 'Full', M-P, MPLIM, ZERO, ZERO,"),
                         (356, "               CALL DLASET( 'Full', MPLIM, P-M, ZERO, ZERO,"),
                         (372, '                  CALL DSWAP( MPLIM-J, UCOEFF(J+1,J,K), 1,'),
                         (385, '      CALL TD03AY( MWORK, PWORK, INDEX, DCOEFF, LDDCOE, UCOEFF, LDUCO1,'),
                         (394, "      CALL TB01PD( 'Minimal', 'Scale', N, MWORK, PWORK, A, LDA, B, LDB,"),
                         (404, "         CALL TB01XD( 'D', NR, MWORK, PWORK, K, NR-1, A, LDA, B, LDB,"),
                         (413, '                  CALL DSWAP( MPLIM-J, UCOEFF(J+1,J,K), 1,')],
            'SB10AD.f': [(506, "         CALL XERBLA( 'SB10AD', -INFO )"),
                         (541, "      CALL DLACPY( 'Full', N, M, B, LDB, DWORK, N )"),
                         (543, "      CALL DLACPY( 'Full', NP, N, C, LDC, DWORK( IWC ), NP )"),
                         (545, "      CALL DLACPY( 'Full', NP, M, D, LDD, DWORK( IWD ), NP )"),
                         (563, '      CALL SB10PD( N, M, NP, NCON, NMEAS, A, LDA, DWORK, N,'),
                         (592, "         CALL DLACPY( 'Full', NP11, M1, DWORK(IWD), LDD, DWORK(IWD1),"),
                         (594, "         CALL DGESVD( 'N', 'N', NP11, M1, DWORK(IWD1), NP11,"),
                         (605, "         CALL DLACPY( 'Full', NP1, M11, DWORK(IWD), LDD, DWORK(IWD1),"),
                         (607, "         CALL DGESVD( 'N', 'N', NP1, M11, DWORK(IWD1), NP1, DWORK(IWS2),"),
                         (654, '         CALL SB10QD( N, M, NP, NCON, NMEAS, GAMMA, A, LDA, DWORK, N,'),
                         (664, '         CALL SB10RD( N, M, NP, NCON, NMEAS, GAMMA, A, LDA, DWORK, N,'),
                         (677, '         CALL SB10LD( N, M, NP, NCON, NMEAS, A, LDA, B, LDB, C, LDC, D,'),
                         (690, "         CALL DLACPY( 'Full', 2*N, 2*N, AC, LDAC, DWORK(IWAC), 2*N )"),
                         (692, "         CALL DGEES( 'N', 'N', SELECT, 2*N, DWORK(IWAC), 2*N, IWORK,"),
                         (764, '      CALL SB10QD( N, M, NP, NCON, NMEAS, GAMMA, A, LDA, DWORK, N,'),
                         (792, '      CALL SB10RD( N, M, NP, NCON, NMEAS, GAMMA, A, LDA, DWORK, N,'),
                         (813, '      CALL SB10LD( N, M, NP, NCON, NMEAS, A, LDA, B, LDB, C, LDC, D,')],
            'SB10HD.f': [(312, "         CALL XERBLA( 'SB10HD', -INFO )"),
                         (344, "      CALL DLACPY( 'Full', N, M, B, LDB, DWORK, N )"),
                         (345, "      CALL DLACPY( 'Full', NP, N, C, LDC, DWORK( IWC ), NP )"),
                         (346, "      CALL DLACPY( 'Full', NP, M, D, LDD, DWORK( IWD ), NP )"),
                         (351, '      CALL SB10UD( N, M, NP, NCON, NMEAS, DWORK, N, DWORK( IWC ), NP,'),
                         (369, '      CALL SB10VD( N, M, NP, NCON, NMEAS, A, LDA, DWORK, N,'),
                         (381, '      CALL SB10WD( N, M, NP, NCON, NMEAS, A, LDA, DWORK, N,')],
            'SB02MD.f': [(395, "         CALL XERBLA( 'SB02MD', -INFO )"),
                         (423, '      CALL SB02MU( DICO, HINV, UPLO, N, A, LDA, G, LDG, Q, LDQ, S, LDS,'),
                         (439, "            CALL DLASCL( 'G', 0, 0, QNORM, GNORM, N, N, S(NP1,1), N2,"),
                         (441, "            CALL DLASCL( 'G', 0, 0, GNORM, QNORM, N, N, S(1,NP1), N2,"),
                         (453, "            CALL DGEES( 'Vectors', 'Sorted', SB02MV, N2, S, LDS, NROT,"),
                         (456, "            CALL DGEES( 'Vectors', 'Sorted', SB02MR, N2, S, LDS, NROT,"),
                         (461, "            CALL DGEES( 'Vectors', 'Sorted', SB02MW, N2, S, LDS, NROT,"),
                         (464, "            CALL DGEES( 'Vectors', 'Sorted', SB02MS, N2, S, LDS, NROT,"),
                         (468, '            CALL DSWAP( N, WR, 1, WR(NP1), 1 )'),
                         (469, '            CALL DSWAP( N, WI, 1, WI(NP1), 1 )'),
                         (489, "      CALL DLACPY( 'Full', N, N, U, LDU, S(NP1,1), LDS )"),
                         (490, '      CALL DGETRF( N, N, S(NP1,1), LDS, IWORK, INFO )'),
                         (504, "      CALL DGECON( '1-norm', N, S(NP1,1), LDS, UNORM, RCOND,"),
                         (518, '         CALL DCOPY( N, U(NP1,I), 1, Q(I,1), LDQ )'),
                         (521, "      CALL DGETRS( 'Transpose', N, N, S(NP1,1), LDS, IWORK, Q, LDQ,"),
                         (526, "      CALL DLASET( 'Full', N, N, ZERO, ZERO, S(NP1,1), LDS )"),
                         (531, '         CALL DAXPY( N-I, ONE, Q(I,I+1), LDQ, Q(I+1,I), 1 )'),
                         (532, '         CALL DSCAL( N-I, HALF, Q(I+1,I), 1 )'),
                         (533, '         CALL DCOPY( N-I, Q(I+1,I), 1, Q(I,I+1), LDQ )'),
                         (541, "     $      CALL DLASCL( 'G', 0, 0, GNORM, QNORM, N, N, Q, LDQ, IERR )")],
            'TB01PD.f': [(249, "         CALL XERBLA( 'TB01PD', -INFO )"),
                         (276, "         CALL TB01ID( 'A', N, M, P, MAXRED, A, LDA, B, LDB, C, LDC,"),
                         (294, "         CALL TB01UD( 'No Z', N, M, P, A, LDA, B, LDB, C, LDC, NCONT,"),
                         (309, "         CALL AB07MD( 'Z', NCONT, M, P, A, LDA, B, LDB, C, LDC, DWORK,"),
                         (317, "         CALL TB01UD( 'No Z', NCONT, P, M, A, LDA, B, LDB, C, LDC, NR,"),
                         (334, "         CALL TB01XD( 'Zero D', NR, P, M, KL, MAX( 0, NR-1 ), A, LDA,")],
            'SB02OD.f': [(559, "         CALL XERBLA( 'SB02OD', -INFO )"),
                         (632, '         CALL DLASCL( QTYPE, 0, 0, QSCAL, ONE, NP, N, Q, LDQ, INFO1 )'),
                         (633, '         CALL DLASCL( RTYPE, 0, 0, RSCAL, ONE, MP, M, R, LDR, INFO1 )'),
                         (635, "     $      CALL DLASCL( 'G', 0, 0, SCALE, ONE, N, M, L, LDL, INFO1 )"),
                         (644, "      CALL SB02OY( 'Optimal control', DICO, JOBB, FACT, UPLO, JOBL,"),
                         (653, '         CALL DLASCL( QTYPE, 0, 0, ONE, QSCAL, NP, N, Q, LDQ, INFO1 )'),
                         (654, '         CALL DLASCL( RTYPE, 0, 0, ONE, RSCAL, MP, M, R, LDR, INFO1 )'),
                         (656, "     $      CALL DLASCL( 'G', 0, 0, ONE, SCALE, N, M, L, LDL, INFO1 )"),
                         (684, "               CALL DLASCL( 'G', 0, 0, SCALE, RNORM, N, N, S(NP1,1),"),
                         (686, "               CALL DLASCL( 'G', 0, 0, RNORM, SCALE, N, N, T(1,NP1),"),
                         (689, "               CALL DLASCL( 'G', 0, 0, SCALE, -RNORM, N, N, S(NP1,1),"),
                         (691, "               CALL DLASCL( 'G', 0, 0, RNORM, SCALE, N, N, S(1,NP1),"),
                         (693, "               CALL DLASCL( 'G', 0, 0, ONE, -ONE, N, N, S(NP1,NP1),"),
                         (698, "               CALL DLASCL( 'G', 0, 0, ONE, -ONE, N, NN, S(NP1,1), LDS,"),
                         (719, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OV, NN, T,"),
                         (722, '            CALL DSWAP( N, ALFAR(NP1), 1, ALFAR, 1 )'),
                         (723, '            CALL DSWAP( N, ALFAI(NP1), 1, ALFAI, 1 )'),
                         (724, '            CALL DSWAP( N, BETA (NP1), 1, BETA,  1 )'),
                         (726, "            CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OV, NN, S,"),
                         (733, "               CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OW, NN,"),
                         (737, "               CALL DGGES( 'No vectors', 'Vectors', 'Sort', SB02OU, NN,"),
                         (743, "               CALL DGEES( 'Vectors', 'Sort', SB02MV, NN, S, LDS, NDIM,"),
                         (747, "               CALL DGEES( 'Vectors', 'Sort', SB02MR, NN, S, LDS, NDIM,"),
                         (752, '            CALL DCOPY( NN, DUM, 0, BETA, 1 )'),
                         (777, '         CALL DCOPY( N, U(NP1,J), 1, X(J,1), LDX )'),
                         (780, "      CALL DLACPY( 'Full', N, N, U, LDU, S(NP1,1), LDS )"),
                         (788, '      CALL DGETRF( N, N, S(NP1,1), LDS, IWORK, INFO1 )'),
                         (805, "         CALL DGECON( '1-norm', N, S(NP1,1), LDS, UNORM, RCOND, DWORK,"),
                         (816, "         CALL DGETRS( 'Transpose', N, N, S(NP1,1), LDS, IWORK, X, LDX,"),
                         (821, "         CALL DLASET( 'Full', N, N, ZERO, ZERO, S(NP1,1), LDS )"),
                         (844, '            CALL DAXPY( N-I+1, ONE, X(I,I), LDX, X(I,I), 1 )'),
                         (845, '            CALL DSCAL( N-I+1, SCALE, X(I,I), 1 )'),
                         (846, '            CALL DCOPY( N-I+1, X(I,I), 1, X(I,I), LDX )')],
            'SB01BD.f': [(326, "         CALL XERBLA( 'SB01BD', -INFO )"),
                         (366, "      CALL DGEES( 'Vectors', 'No ordering', SELECT, N, A, LDA, NCUR,"),
                         (385, "      CALL MB03QD( DICO, 'Stable', 'Update', N, 1, N, ALPHA,"),
                         (392, "      CALL DLASET( 'Full', M, N, ZERO, ZERO, F, LDF )"),
                         (467, "            CALL DGEMM( 'Transpose', 'NoTranspose', IB, M, N, ONE,"),
                         (513, '                        CALL DLAEXC( .TRUE., N, A, LDA, Z, LDZ, NSUP-2,'),
                         (535, "               CALL DGEMM( 'Transpose', 'NoTranspose', IB, M, N, ONE,"),
                         (564, '                     CALL SB01BX( .TRUE., NPR, X, X, WR, X, S, P )'),
                         (576, '                        CALL MB03QY( N, NL, A, LDA, Z, LDZ, X, Y, INFO )'),
                         (578, '                           CALL SB01BX( .FALSE., NPC, X, Y,'),
                         (586, '                           CALL SB01BX( .TRUE., NPR, X, X, WR, X, S, P )'),
                         (587, '                           CALL SB01BX( .TRUE., NPR-1, X, X, WR, X,'),
                         (600, '                        CALL SB01BX( .FALSE., NPC, X, ZERO, WR(IPC),'),
                         (621, '                  CALL SB01BY( IB, M, S, P, A2, DWORK(KG), DWORK(KFI),'),
                         (647, '                        CALL DROT( N-NL+1, A(NL,NL), LDA,'),
                         (649, '                        CALL DROT( N, A(1,NL), 1, A(1,NSUP), 1, C, S )'),
                         (650, '                        CALL DROT( N, Z(1,NL), 1, Z(1,NSUP), 1, C, S )'),
                         (667, "                     CALL DGEMM( 'NoTranspose', 'Transpose', M, N,"),
                         (679, "                     CALL DGEMM( 'NoTranspose', 'NoTranspose', N, IB,"),
                         (682, "                     CALL DGEMM( 'Transpose', 'NoTranspose', NSUP,"),
                         (689, '     $                  CALL MB03QY( N, NL, A, LDA, Z, LDZ, X, Y,'),
                         (717, '                              CALL DLAEXC( .TRUE., N, A, LDA, Z, LDZ,'),
                         (756, "     $   CALL DLASET( 'L', N-2, N-2, ZERO, ZERO, A(3,1), LDA )"),
                         (763, '         IF( K .GT. 0 ) CALL DSWAP( K, WR(NPR+1), 1, WR, 1 )'),
                         (766, '            CALL DSWAP( J, WR(IPC+NPC), 1, WR(K+1), 1 )'),
                         (767, '            CALL DSWAP( J, WI(IPC+NPC), 1, WI(K+1), 1 )')],
            'AB09AD.f': [(303, "         CALL XERBLA( 'AB09AD', -INFO )"),
                         (330, "         CALL TB01ID( 'A', N, M, P, MAXRED, A, LDA, B, LDB, C, LDC,"),
                         (338, '      CALL TB01WD( N, M, P, A, LDA, B, LDB, C, LDC, DWORK(KT), N,'),
                         (349, '      CALL AB09AX( DICO, JOB, ORDSEL, N, M, P, NR, A, LDA, B, LDB, C,')]}}
        self.f = find_slycot.FindFunctionUsedFortran(self.result_dict)

    def test_handle_file(self):
        args = ('SB04MD.f', "         CALL XERBLA( 'SB04MD', -INFO )", 196,
                os.path.join('..', '..', 'slycot', 'slycot', 'src'))
        self.f.handle_file(*args)
        expected = [('slycot\\src', 'SB04MD.f', 196)]
        self.assertSequenceEqual(expected, self.f.function_names['xerbla'])


if __name__ == '__main__':
    unittest.main()
