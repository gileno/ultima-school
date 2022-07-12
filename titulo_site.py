from requests_html import HTMLSession
sessao = HTMLSession()
site = input("Qual o site que deseja saber o título: ")
resposta = sessao.get(site)
tag_inicio = "<title"
tag_fim = "</title>"
titulo = resposta.text[resposta.text.index(tag_inicio):resposta.text.index(tag_fim)].replace("<title>", "")
print(titulo)
