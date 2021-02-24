from timeit import default_timer
from math import sqrt

def TestaPrimo(n):
    EhPrimo = 1
    d=2
    if (n <= 1):
        EhPrimo = 0

    while EhPrimo == 1 and d <= n / 2:
        if n % d  == 0:
            EhPrimo = 0
        d = d + 1

    return EhPrimo;

def testa_primo1(n):
	if n <= 1:
		return 0

	for d in range(2, n/2):
		if n % d == 0:
			return 0

	return 1

numeros_avaliados = [7, 37, 8431, 13033, 524287, 664283, 3531271, 2147483647]
tempos_medios = {}
desvios_padroes = {}

for numero in numeros_avaliados:
	tempos = []
	for i in range(10):
		inicio = default_timer()
		eh_primo = TestaPrimo(numero)
		fim = default_timer()
		tempos.append(fim - inicio)
	print(str(numero) + (int(eh_primo) and ' eh primo' or ' nao eh primo'))

	tempos_medios[str(numero)] = sum(tempos) / 10

	desvios_padroes[str(numero)] = sqrt(sum([((tempo - tempos_medios[str(numero)]) ** 2) for tempo in tempos]))

for tempo in tempos_medios:
	print('Tempo medio de execucao (em ms) para o numero {}: {:4.10f}'.format(tempo, tempos_medios[tempo]))
	print('Desvio padrao para o numero {}: {:4.10f}'.format(tempo, desvios_padroes[tempo]))
