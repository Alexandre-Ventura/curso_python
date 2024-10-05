
def area_cilindro(raio, altura):
    
    def area_circulo(raio):
        PI = 3.141592
        area = PI * pow(raio, 2)
        return area
    
    area = area_circulo(raio) * altura
    return area

h = float(input("Qual o valor da altura? "))
r = float(input("Qual o valor do raio? "))
a = area_cilindro(r, h)

print(f"O valor da area do cilindro é {a:.2f}")