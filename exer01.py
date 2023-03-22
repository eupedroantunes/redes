import math

"""
Download Típico:                   Download Melhor: 
T = S/P                            T = S/BW
------------------------------------------------------
T = TIME TO DOWNLOAD IN SECONDS
S = SIZE OF THE FILE
P = THROUGHPUT
BW = BANDWIDTH
"""

"""
1) Para calcular o tempo necessário para transferir um arquivo de 500 MB em
uma rede local com uma vazão de 100 Mbps, podemos utilizar a seguinte
fórmula: Tempo de transferência = (tamanho do arquivo em bits) / Throughput
"""
print("Exercício 01")
t = (500 * 8) / 100
# print(f'{t} segundos')

if t > 60:
    minutos = t % 60
    segundos = t // 60
    print(f'{t:.0f} segundos ou {minutos:.0f} min e {segundos:.0f} segundos')
else:
    print(f'{t:.0f} segundos')


"""
2) Em um servidor local com Bandwidth de 100.000 kbps, foi necessário
transferir um arquivo de 3.3 GB, quanto tempo demorou ?
"""
print("Exercício 02")
bw = 100_000 # in kbps
s = ((3.3 * 1000) * 1000) * 8 # GB -> MB -> KB -> Kbits

t = s/bw
# print(f'{t} segundos') # = 264 segundos

if t > 60:
    minutos = t // 60
    segundos = t % 60
    print(f'{t:.0f} segundos ou {minutos:.0f} min e {segundos:.0f} segundos')
else:
    print(f'{t:.0f} segundos')

"""
3) Suponha que você precise transferir um arquivo de 1 GB (gigabyte) pela
Internet. Sabendo que a sua conexão tem uma velocidade de download de
10 Mbps (megabits por segundo), qual seria o tempo estimado para realizar
essa transferência ?
"""

print("Exercício 03")
s = (1 * 1000) * 8 # GB -> MB -> Mbits
p = 10

t = s/p

if t > 60:
    minutos = t // 60
    segundos = t % 60
    print(f'{t:.0f} segundos ou {minutos:.0f} min e {segundos:.0f} segundos')
else:
    print(f'{t:.0f} segundos')

"""
4) Caso você tenha uma conexão de Internet com velocidade de upload de 5
Mbps e, seja preciso enviar um vídeo de 500 MB (megabytes) para um
amigo. Qual seria o tempo estimado para realizar essa transferência?
"""
print("Exercício 04")
s = 500 * 8
p = 5

t = s/p

if t > 60:
    minutos = t // 60
    segundos = t % 60
    print(f'{t:.0f} segundos ou {minutos:.0f} min e {segundos:.0f} segundos')
else:
    print(f'{t:.0f} segundos')

"""
5) Em uma LAN, é necessário transferir um arquivo comprimido de tamanho 250
MB, do seu PC que possui a placa de rede com 1Gbit/s para outro notebook
que fora testado o Throughput de 600 kbps, qual estimativa de tempo para
isto ?
"""
print("Exercício 05")
s = (250 * 1000) * 8 # MB -> KB -> Kbits
p = 600

t = s/p

if t > 60:
    minutos = t // 60
    segundos = t % 60
    print(f'{t:.0f} segundos ou {minutos:.0f} min e {segundos:.0f} segundos')
else:
    print(f'{t:.0f} segundos')