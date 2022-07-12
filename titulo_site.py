from requests_html import HTMLSession
sessao = HTMLSession()
site = input("Qual o site que deseja saber o título: ")
resposta = sessao.get(site)
tag_inicio = "<title>"
tag_fim = "</title>"
inicio_titulo = resposta.text.index(tag_inicio) + 7
fim_titulo = resposta.text.index(tag_fim)
titulo = resposta.text[inicio_titulo:fim_titulo]
print(titulo)
