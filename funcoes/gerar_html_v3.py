def tag_block(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join( f'<li>{item}</li>' for item in itens )
    return f'<ul>{lista}</ul>'


if __name__ == "__main__":
    lista_nomes = ['Ana', 'Felipe', 'Marina', 'Junior', 'Decir']
    lista = tag_lista(*lista_nomes)
    block = tag_block(conteudo=lista, inline=True)

    print(block)