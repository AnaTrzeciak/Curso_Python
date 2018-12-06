#ecoding:utf-8
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

habitantesA= float(input("Habitantes do país A:"))
habitantesB= float(input("Habitantes do país B:"))

taxaA= float(input("Taxa de crescimento do país A (%):"))
taxaB= float(input("Taxa de crescimento do país B (%):"))

print("O país A aumenta ",(habitantesA*(taxaA/100.0))," pessoas por ano.\n")
print("O país B aumenta ",(habitantesB*(taxaB/100.0))," pessoas por ano.\n")


