def tag_block(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == "__main__":
    bloco = tag_block('Erro ao autenticar usuário', 'danger', inline=True)
    print(bloco)