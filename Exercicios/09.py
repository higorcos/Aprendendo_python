celsus = float(input('Qual a temperatura atua em celsus: '))
#convertendo 
fahrenheit = (celsus*9/5)+32
kelvin = celsus + 273.15 
print('Os {}°C representão {}° Fahrenheit e {:.2f} na escala Kevin'.format(celsus,fahrenheit,kelvin))