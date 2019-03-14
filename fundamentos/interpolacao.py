from string import Template

nome, idade = 'Ana', 30.9875

print('Nome: %s, Idade: %.2f' % (nome, idade))
print('Nome: {}, Idade: {}'.format(nome, idade))
print(f'Nome: {nome}, Idade: {idade}')  # python >= 3.6

s = Template('Nome: $n, Idade: $i')
print(s.substitute(n=nome, i=idade))
