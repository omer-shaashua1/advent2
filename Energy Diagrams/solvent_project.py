from energydiagram import ED
import matplotlib.pyplot as plt


diagram = ED()
diagram.round_energies_at_digit = 2
diagram.bottom_text_fontsize = 'small'
diagram.top_text_fontsize = 'small'
diagram.offset = 2


# Toluene Values:
A2_TOL = 0.0
B2_TOL = 9.464718247
T2_OA_TOL = 20.98829352
C2_TOL = -18.537605
T2_LS_TOL = -11.09922
E2_TOL = -10.72774
T2_TM_TOL = 15.1685575
G2_TOL = -33.404335
T2_RE_TOL = -17.4877975
A_prime_TOL = -60.4602525

# DMSO Values:
A2_DMSO = 0.0
B2_DMSO= 10.19513872
T2_OA_DMSO = 21.71934151
C2_DMSO = -22.0923925
T2_LS_DMSO = -9.1909925
E2_DMSO = -18.1065125
T2_TM_DMSO = 10.0506675
G2_DMSO = -35.751185
T2_RE_DMSO = -19.822725
A_prime_DMSO = -63.265805

# this is the energy levels
diagram.add_level(0, 'A2')

diagram.add_level(7.947401485, 'B2', color='g')
diagram.add_level(B2_TOL,"", 'last', color="b")
diagram.add_level(B2_DMSO,"", 'last', color="r")

diagram.add_level(19.8597475, 'OA', color='g')
diagram.add_level(T2_OA_TOL,"", 'last', color="b")
diagram.add_level(T2_OA_DMSO,"", 'last', color="r")

diagram.add_level(-16.248485, '', color='g')
diagram.add_level(C2_TOL,"", 'last', color="b")
diagram.add_level(C2_DMSO,"C2", 'last', color="r")

diagram.add_level(-19.59306, 'LS', color='g')
diagram.add_level(T2_LS_TOL,"", 'last', color="b")
diagram.add_level(T2_LS_DMSO,"", 'last', color="r")

diagram.add_level(-5.64499, '', color='g')
diagram.add_level(E2_TOL,"", 'last', color="b")
diagram.add_level(E2_DMSO,"E2", 'last', color="r")

diagram.add_level(22.0258775, '', color='g')
diagram.add_level(T2_TM_TOL,"", 'last', color="b")
diagram.add_level(T2_TM_DMSO,"TM", 'last', color="r")

diagram.add_level(-24.2968, '', color='g')
diagram.add_level(G2_TOL,"", 'last', color="b")
diagram.add_level(G2_DMSO,"G2", 'last', color="r")

diagram.add_level(-12.0084675, '', color='g')
diagram.add_level(T2_RE_TOL,"", 'last', color="b")
diagram.add_level(T2_RE_DMSO,"RE", 'last', color="r")

diagram.add_level(-52.831735, "", color='g')
diagram.add_level(A_prime_TOL,"", 'last', color="b")
diagram.add_level(A_prime_DMSO,"A'2", 'last', color="r",)

#linking the energy levels
diagram.add_link(0, 1, color='g')
diagram.add_link(0, 2, color='b')
diagram.add_link(0, 3, color='r')

diagram.add_link(1, 4, color='g', linestyle=':')
diagram.add_link(4, 7, color='g')
diagram.add_link(7, 10, color='g')
diagram.add_link(10, 13, color='g')
diagram.add_link(13, 16, color='g')
diagram.add_link(16, 19, color='g')
diagram.add_link(19, 22, color='g')
diagram.add_link(22, 25, color='g')


diagram.add_link(2, 5, color='b')
diagram.add_link(5, 8, color='b')
diagram.add_link(8, 11, color='b')
diagram.add_link(11, 14, color='b')
diagram.add_link(14, 17, color='b')
diagram.add_link(17, 20, color='b')
diagram.add_link(20, 23, color='b')
diagram.add_link(23, 26, color='b')


diagram.add_link(3, 6, color='r')
diagram.add_link(6, 9, color='r')
diagram.add_link(9, 12, color='r')
diagram.add_link(12, 15, color='r')
diagram.add_link(15, 18, color='r')
diagram.add_link(18, 21, color='r')
diagram.add_link(21, 24, color='r')
diagram.add_link(24, 27, color='r')


#arrows for RDS
diagram.add_arrow(7, 16, position='left', color='g')
diagram.add_arrow(8, 17, position='left', color='b')
diagram.add_arrow(9, 18, position='left', color='r')



diagram.offset = 0.10
# diagram.plot(show_IDs=True)
diagram.plot(ylabel="Energy / $kcal$ $mol^{-1}$") # this is the default ylabel
plt.show()