from compartment import Compartment


# a simple artery %TODO implement
class Artery(Compartment):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        R = 1000.             # viscosity
        L = 300                 # inertia
        C = 100. / R             # compliance
        Q1 = 0.0003             # boundary Q  0.3 mm/s
        Q2 = 0.0003             # initial Q2
        P1 = 10000.              # initial P1 10kPa
        P2 = 10000.              # boundary P
        # call parent constructor with default values
        super(Artery, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
