from timeit import default_timer
from math import sqrt
import eh_primo

numeros_avaliados = [7, 37, 8431, 13033, 524287, 664283, 3531271, 2147483647]
infos = []
algoritmos = ['TestaPrimo', 'testa_primo2', 'testa_primo3']

for numero in numeros_avaliados:
    for alg in algoritmos:
        print('algoritmo: {}, numero: {}'.format(alg, numero))
        algoritmo = getattr(eh_primo, alg, None)
        tempos = []
        for i in range(30):
            inicio = default_timer()
            primo = algoritmo(numero)
            fim = default_timer()
            tempos.append((fim - inicio) * 1000) # multiplicando por 1000 ja na definicao para ficar em ms tanto no calculo de tempo medio quanto de desvio padrao
        tempo_medio = (sum(tempos) / 30.0)
        desvio_padrao = sqrt(sum([(tempo - tempo_medio) ** 2 for tempo in tempos]) / 30)

        infos.append({'numero': numero, 'algoritmo': str(alg), 'tempo_medio': tempo_medio, 'desvio_padrao': desvio_padrao, 'primo': primo})

# Calcula speedup
for numero in numeros_avaliados:
    # informacoes do numero para os 2 algoritmos adicionais
    lista_infos_numero = list(filter(lambda x : x['numero'] == numero and x['algoritmo'] != 'TestaPrimo', [info for info in infos]))
    # informacoes do numero para o algoritmo de referencia
    infos_numero_referencia = list(filter(lambda x : x['numero'] == numero and x['algoritmo'] == 'TestaPrimo', [info for info in infos]))[0]
    
    for info_numero in lista_infos_numero:
        speedup = infos_numero_referencia['tempo_medio'] / info_numero['tempo_medio']
        infos[infos.index(info_numero)]['speedup'] = speedup

with open('saida.txt', 'w') as file:
    for item in infos:
        file.writelines(str(item) + '\r\n')
    file.close()
