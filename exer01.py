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
t = 500 / 100
print(f'{t} segundos')

"""
2) Em um servidor local com Bandwidth de 100.000 kbps, foi necessário
transferir um arquivo de 3.3 GB, quanto tempo demorou ?
"""
print("Exercício 02")
bw = 100_000 # in kbps
sInGB = 3.3 # in GB
sInMB = sInGB * 1000 # in MB
sInKB = sInMB * 1000 # in KB
s = sInKB * 8

t = s/bw
print(f'{t} segundos') # = 264 segundos

"""
3) Suponha que você precise transferir um arquivo de 1 GB (gigabyte) pela
Internet. Sabendo que a sua conexão tem uma velocidade de download de
10 Mbps (megabits por segundo), qual seria o tempo estimado para realizar
essa transferência ?
"""

print("Exercício 03")
sInGB = 1
sInMB = sInGB * 1000
s = sInMB * 8
p = 10

t = s/p
print(f'{t} segundos')

"""
4) Caso você tenha uma conexão de Internet com velocidade de upload de 5
Mbps e, seja preciso enviar um vídeo de 500 MB (megabytes) para um
amigo. Qual seria o tempo estimado para realizar essa transferência?
"""
print("Exercício 04")
sInMB = 500 * 8
p = 5

t = s/p
print(f'{t} segundos')