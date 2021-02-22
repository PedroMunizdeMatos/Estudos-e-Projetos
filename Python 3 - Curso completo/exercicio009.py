l = float(input('Qual a Largura da parede em metros?: '))
h = float(input('E qual é a altura em metros?: '))
a = l * h
t = a/2
print('sua parede de altura {}m e largura {}m tem {}m² de área.'.format(h, l, a))
print('Portanto, serão necessários {}L de tinta para cobri-la completamente.'.format(t))
