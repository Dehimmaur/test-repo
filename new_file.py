v = input('Введите скорость: ')
h = input('Введите время: ')

v = int(v)
h = int(h)

L = h*v 

if L >=109:
	L = L - 109

print('Вы остановитесь на отметке: ' + str(L))


