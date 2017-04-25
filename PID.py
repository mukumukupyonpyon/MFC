
class PID(object):
    def __init__(self,Kc=0.,Ti=1.,Td=0.):
        self.Kc=Kc
        self.Ti=Ti
        self.Td=Td
        self.P=0.
        self.I=0.
        self.D=0.
        self.U=0.
        self.e=[0,0]
        
        
    def u(self,e,dt):
        self.P=self.Kc*(e-self.e[0])
        self.I=self.Kc/self.Ti*dt*e
        self.D=self.Kc*self.Td/dt*(e-2*self.e[0]+self.e[1])
        self.U+=self.P+self.I+self.D
        self.e[1]=self.e[0];self.e[0]=e
        return self.U


    
