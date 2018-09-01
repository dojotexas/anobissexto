from bissexto import bissexto

for i in range(1000,3300,4):
    if bissexto(i):
        print('Ano {} Bissexto'.format(i))