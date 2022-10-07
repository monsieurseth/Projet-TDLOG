class Math:
    def __init__(self,n):
        self.n =n
    def factoriel(self):
        self.fact = 1
        if self.n== 0:
            return f"{self.n}! = 1"
        else:
            for i in range(1,self.n+1):
                self.fact *=i
            return f"{self.n}! = {self.fact}"