from oops_concept.demoa import A
from oops_concept.demob import B

class C(A, B):
    def __init__(self, n1, n2, msg):
        A.__init__(self, n1, n2)
        B.__init__(self, msg = msg)

    def final(self):
        print("Done")