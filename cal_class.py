from unittest import result


class cal:
    def __init__(self, no1,no2):
        self.no1=no1
        self.no2=no2
    
    def add(self):
        return self.no1 + self.no2
        
    def sub(self):
        return self.no1 - self.no2
    
    def mul(self):
        return self.no1 * self.no2
    
    def div(self):
        return self.no1 / self.no2

x= cal(20,10)
result=x.add()
print(result)

result=x.sub()
print(result)

result=x.mul()
print(result)

result=x.div()
print(result)