#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_atrs')

def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items() if k in suportados)

def tag_block(conteudo, *args,classe='success', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = get_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **kwargs):
    lista = ''.join( f'<li>{item}</li>' for item in itens )
    return f'<ul {get_atrs(kwargs, ul_atrs)} >{lista}</ul>'


if __name__ == "__main__":
    print(tag_block(tag_lista, 'Item 1', 'Item 2', classe='info', bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))