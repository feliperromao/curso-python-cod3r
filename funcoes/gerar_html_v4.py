def tag_block(conteudo, *args,classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join( f'<li>{item}</li>' for item in itens )
    return f'<ul>{lista}</ul>'


if __name__ == "__main__":
    block = tag_block(tag_lista, 'Ana', 'Felipe', 'Marina', 'Junior', 'Decir',
                      classe='info', inline=True)
    print(block)