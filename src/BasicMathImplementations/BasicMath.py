class MathFunctions:
    def __init__(self) -> None:
        pass

#GCD/HCF of two numbers a,b
    def gcd(self,a,b)->int:
        if b<a:
            a,b=b,a
        while a:
            a,b=b%a,a        
        return b
    
#LCM of two numbers a,b
    def lcm(self,a,b)->int:
        return (a*b)//(self.gcd(a,b))