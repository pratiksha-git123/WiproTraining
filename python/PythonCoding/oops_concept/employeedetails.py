class EmployeeDetails:
    def __init__(self, empno, empname, basicpay):
        self.empno = empno
        self.empname = empname
        self.basicpay = basicpay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

        # def get_empno(self):
        #     return self.__empno
        # def set_empno(self, eno):
        #     self.__empno = eno

        @property
        def empno(self):
            return self.__empno
        @empno.setter
        def empno(self, eno):
            self.__empno = eno

        @property
        def empname(self):
            return self.__empname
        @empname.setter
        def empname(self, en):
            self.__empname = en

        @property
        def basicpay(self):
            return self.__basic_pay
        @basicpay.setter
        def basicpay(self, bp):
            self.__basic_pay = bp



    def calculate_allowance(self):
       allowance = (self.basicpay * self.da / 100) + (self.basicpay * self.hra / 100)
       return allowance

    def calculate_deduction(self):
       deduction = (self.basicpay * self.pf / 100)
       return deduction

    def calculate_netsal(self):
        netsal = self.basicpay + self.calculate_allowance() - self.calculate_deduction()
        return netsal


