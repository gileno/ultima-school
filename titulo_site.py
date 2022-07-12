from requests_html import HTMLSession
sessao = HTMLSession()
site = input("Qual o site que deseja saber o título: ")
resposta = sessao.get(site)
inicio_titulo = resposta.text.index("<title>")
fim_titulo = resposta.text.index("</title>")
titulo = resposta.text[inicio_titulo:fim_titulo].replace("<title>", "")
print(titulo)
