#ecoding:utf-8
#Crie um programa que exiba todos as horas, segundos e minutos  no seguinte formato: ZZh XXmin YYs


for horas in range(24):
  for minutos in range(60):
    for segundos in range(60):
      print(horas,"h",minutos,"min",segundos,"s")
