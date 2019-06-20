class Carro():
    def __init__ (self, num):
        self.consumo = num
        
    def adicionarGasolina(self, gasol):
        self.gasolina=gasol
        
    def andar(self, dist):
        self.gasolina=self.gasolina-((self.gasolina*dist)/(self.consumo*self.gasolina))

    def obterGasolina(self):
        print('Ainda restam %.4f litros no tanque' % self.gasolina)

minhaF250=Carro(15)
minhaF250.adicionarGasolina(20)
minhaF250.andar(100)
minhaF250.obterGasolina()
        
        

        
