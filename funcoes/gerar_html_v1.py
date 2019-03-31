def tag_block(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == "__main__":
    bloco = tag_block('Erro ao autenticar usuário', 'danger')
    print(bloco)