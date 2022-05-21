#operador primirivo = +,-,*,/
class reloj():
    def __init__ (self,h,m,s):
        self.hora = h
        self.minuto = m
        self.segundo = s
    def __str__ (self):
        return str(self.hora) + " Horas " + str(self.minuto) + " Minutos " + str(self.segundo) + " Segundos "
    
    def mostrar (self):
        print("Reloj: ", self.hora, "Horas", self.minuto, "minutos", self.segundo, "Segundos")

    def __add__ (self,t1):
        hh = self.hora + t1.hora
        mm = self.minuto + t1.minuto
        ss = self.segundo + t1.segundo
        if ss > 60:
            ss = ss - 60
            mm = mm + 1
        if mm > 60:
            mm = mm - 60
            hh = hh + 1
        
        return reloj(hh,mm,ss)


def main():
    h1 = reloj(5,40,30)
    h2 = reloj(2,30,25)
    h3 = h1 + h2
    print ( h3)

main()