# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from os import system as executa
def instalarPip():
    executa('sudo apt-get install python3-pip')
def instalarDependencia():
    executa('pip3 install urllib')
    executa('pip3 install oauth2')
    executa('pip3 install requests')
    executa('pip3 install emoji')
    executa('pip3 install bs4')
    executa('pip3 install json')
try:
    import urllib
    from urllib.request import quote as pegarDados, urlopen as lerHtml
    from urllib.error import HTTPError as erroHttp
    from oauth2 import Consumer, Client, Token
    from requests import post as pegarLink
    from emoji import emojize as carinha
    from bs4 import BeautifulSoup as sopa
    from json import loads as lerJson
except :
    try:
        print("Instalando Dependencias")
        instalarDependencia()
        try:
            print("Instalando Pip3")
            instalarPip()
            instalarDependencia()
        except:
            print("Falha na instalação do Pip3 e Dependencias")
    except :
        print("")
    print("")
    from urllib.request import quote as pegarDados, urlopen as lerHtml
    from oauth2 import Consumer, Client, Token
    from requests import post as pegarLink
    from emoji import emojize as carinha
    from bs4 import BeautifulSoup as sopa
    from json import loads as lerJson
    print('')
executa('clear')
#=============================Variaveis Globais
def lerArquivoSenha(nomeArquivo,apagar=False):
    if apagar == True:
        print('''======================================================================
==               Arquivo de senhas está apagado                    == 
======================================================================
''')
        arquivoSenha = open(nomeArquivo, 'w')
        arquivoSenha.write(input("Digite sua chave:") + '\n')
        arquivoSenha.write(input("Digite sua chave Secreta:") + '\n')
        arquivoSenha.write(input("Digite seu Token:") + '\n')
        arquivoSenha.write(input("Digite seu Token Secreto:") + '\n')
        arquivoSenha.close()
    else:
        try:
            arquivoSenha = open(nomeArquivo,'r')
            senhas = []
            for linha in arquivoSenha.readlines():
                senhas.append(linha)
            arquivoSenha.close()
            return senhas
        except:
            print(texto)
            arquivoSenha = open(nomeArquivo, 'w')
            arquivoSenha.write(input("Digite sua chave:")+'\n')
            arquivoSenha.write(input("Digite sua chave Secreta:")+'\n')
            arquivoSenha.write(input("Digite seu Token:")+'\n')
            arquivoSenha.write(input("Digite seu Token Secreto:")+'\n')
            arquivoSenha.close()
            arquivoSenha = open(nomeArquivo,'r')
            senhas = []
            for linha in arquivoSenha.readlines():
                senhas.append(linha)
            arquivoSenha.close()
            return senhas
def cadastrarSenha():
    try:
        print('''
====================================================================
==       Para perfeito funcionamento e integração deste  programa ==
== com o Twitter, é necessário informar, sua chave, chave secreta ==
== token e token secreto.                                         ==
====================================================================
-- Acesse https://developer.twitter.com/en/apps para cria um  app --
-- em seguida, crie e pegue suas chaves, atenção  não armazenamos --
-- e não solicitamos estas chaves fora da execução deste programa --
====================================================================
==          Para Apagar senhas ou adcinoar novas senhas           ==
==                      Digite 1 e ENTER                          ==                         
====================================================================
==    Para Continuar com senhas já cadastradas digite ENTER       ==
====================================================================
        ''')
        apagar = input('O quê você deseja fazer?:')
        if apagar == '1':
            executa('clear')
            senha = lerArquivoSenha('senha',apagar=True)
            return senha
        else:
            senha = lerArquivoSenha('senha')
            return senha
    except:
        print("Falha no cadastro de senhas do Twitter")

try:
    senha = cadastrarSenha()
    key_c1 = senha[0].strip()
    key_c_s1 = senha[1].strip()
    token_k1 = senha[2].strip()
    token_k_s1 = senha[3].strip()
except:
    key_c1 = 'senha[0].strip()'
    key_c_s1 = 'senha[1].strip()'
    token_k1 = 'senha[2].strip()'
    token_k_s1 = 'senha[3].strip()'
executa('clear')
sorriso = carinha(":smile:", use_aliases=True)
mundo = 'news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
negocio = 'news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
citec = 'news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSkwyMHZNR1ptZHpWbUVnVndkQzFDVWhvQ1FsSW9BQVAB?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
entretenimento = 'news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
esporte = 'news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
saude = 'news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYQjBMVUpTS0FBUAE?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
brasil = 'news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREUxWm5JU0JYQjBMVUpTS0FBUAE?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
principais = 'news.google.com/?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
Thoje = "twitter.com/i/moments"
Tnoticia = "twitter.com/i/moments?category_id=1"
Tesporte = "twitter.com/i/moments?category_id=2"
Tentretenimento = "twitter.com/i/moments?category_id=3"
Tdiversao = "twitter.com/i/moments?category_id=4"
G1 = "g1.com.br"
UOL = "www.uol.com.br"
TERRA = 'www.terra.com.br/noticias/'
R7 = 'noticias.r7.com/brasil'
EXAME = 'exame.abril.com.br/noticias-sobre/sites/'
BBCbrasil = 'www.bbc.com/portuguese/brasil'
BBCinternacional = 'www.bbc.com/portuguese/internacional'
BBCeconomia = 'www.bbc.com/portuguese/topics/ca170ae3-99c1-48db-9b67-2866f85e7342'
BBCsaude = 'www.bbc.com/portuguese/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2'
BBCciencia = 'www.bbc.com/portuguese/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'
BBCtecnologia = 'www.bbc.com/portuguese/topics/31684f19-84d6-41f6-b033-7ae08098572a'
tamanho=20
#=============================basico para escavar sites
def encurtarLink(link,origem=''):
    site1 = origem + link
    try :
        if origem == '':
            return pegarLink("http://is.gd/api.php?longurl={}".format(link)).text
        else:
            return pegarLink("http://is.gd/api.php?longurl={}".format(site1)).text
    except :
        return "Erro na conversão do link"
def lerSite(site):
    try:
        #função faz o retorno do html do site
        request_headers = {
            "Accept-Language": "pt-br",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html",
            "Referer": "http://www.google.com.br",
            "Connection": "keep-alive"
        }
        html = lerHtml("http://{}".format(site))
        return html.read()
    except :
        print("Erro ao ler o site:{}\nAtenção retire http:// para condicionamento do site".format(site))
def sopaSite(site):
    try:
        #função faz o retorno do objeto do html do site
        a = sopa(lerSite(site), "html.parser")
        return a
    except:
        print("Erro na sopa do site")

def quantasReportagens():
    try:
        total = int(input("Quantas reportagens devemos mostrar:"))
        print('''
Vamos tentar mostrar {} reportagens
Aguarde o levantamento das informações solicitadas, estamos vasculhando a internet...
========================================================'''.format(total))
    except :
        total = 5
        print('''
Quantidade invalida, vamos tentar mostrar 5 reportagens
Aguarde o levantamento das informações solicitadas, estamos vasculhando a internet...
========================================================
        ''')
    return total
def conectarOauthConsumidorGeral(consumidor_chave, consumidor_chave_secreta):
    #Função recebe chave secreta e chave para consumidor da api
    a = consumidor_chave
    b = consumidor_chave_secreta
    return Consumer(a, b)
def conectarOauthTokenGeral(token_chave, token_chave_secreta):
    # função gera token geral para qualquer api que usa OAUTH
    a = token_chave
    b = token_chave_secreta
    return Token(a, b)
#=============================fim do basico para escavar sites
#=============================inicio dos leitores de sites
def oauthTwitter(consumidor_chave, consumidor_chave_secreta, token_chave, token_chave_secreta):
    try:
        # função recebe identificações do twiter, realiza uma conecção pesquisar o que for informado pelo usuario e retorna a informação
        conectar = Client(conectarOauthConsumidorGeral(consumidor_chave, consumidor_chave_secreta),
                          conectarOauthTokenGeral(token_chave, token_chave_secreta))
        pesquisar = urllib.parse.quote(input('O quê vamos procurar no twitter?:'))
        ler = conectar.request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(pesquisar))
        ler_str = ler[1].decode()  # convertendo o objeto em string
        ler_obj = lerJson(ler_str)
        for x in ler_obj['statuses']:
            nome = x['user']['name']
            nomearroba = '@{}'.format(x['user']['screen_name'])
            descricao = x['user']['description']
            criacao = 'Data da Criação: {}'.format(x['user']['created_at'])
            localizacao = 'Pais {}'.format(x['user']['location'])
            localizacao_cidade = 'Cidade: {}'.format(x['user']['time_zone'])
            identificacao = 'Id: {}'.format(x['user']['id'])
            lingua = 'Lingua: {}'.format(x['user']['lang'])
            fotofundo = 'Foto do fundo {}'.format(x['user']['profile_background_image_url'])
            foto = x['user']['profile_image_url_https']
            perfil = x['user']['url']
            print('''========================================================
    Usuario: {} {} {} {}
    Escreveu: {}
    '''.format(nome, nomearroba,localizacao_cidade, criacao, x['text']))
    except:
        print('''======================================================================
  Falha no uso das senhas no Twitter, reinicie o programa para nova 
  leitura do arquivo com as senhas ou para inserir as senhas 
======================================================================
''')
def oauthTwitterEscrever(consumidor_chave, consumidor_chave_secreta, token_chave, token_chave_secreta):
    try:
        # função recebe identificações do twiter, realiza uma conecção e publica no perfil
        conectar = Client(conectarOauthConsumidorGeral(consumidor_chave, consumidor_chave_secreta),
                          conectarOauthTokenGeral(token_chave, token_chave_secreta))
        escrever = urllib.parse.quote(input('O quê vamos escrever no twitter?:'))
        twitter = conectar.request('https://api.twitter.com/1.1/statuses/update.json?status={}'.format(escrever),
                                   method='POST')
        #print(twitter)
    except:
        print('''======================================================================
  Falha no uso das senhas no Twitter, reinicie o programa para nova 
  leitura do arquivo com as senhas ou para inserir as senhas 
======================================================================
        ''')
def lerNoticia(site, tagClasse="", tagSub="", tag="div",tagClasse1="", todoLink=False,  total=10, contagem=1, origem='', tamanhoString=100):
    repetido = ['', 'Inovação', 'Brasil', 'Ciência', 'RD1', 'Telesíntese', 'Revista Planeta', 'Brasil','Aprenda inglês', 'ao vivo', 'Economia', 'História', 'Vídeo', 'Saúde', 'Sociedade', 'últimas', 'hora 7','record tv', 'estrelando', 'ver tudo', 'IstoÉ', 'Mundo', 'DINO', 'Ciência', 'Sustentabilidade','Tecnologia', 'Comportamento', 'Polícia', 'Jornal do Brasil', 'Cidades', 'Política', 'Climatempo']
    if todoLink == False:
        try:
            for x in sopaSite(site).find_all(tag, {"class": tagClasse}, limit=total):
                titulo1 = x.text.strip()[:tamanhoString-20]
                if origem != '':
                    link1 = encurtarLink(x.a['href'],origem)
                else:
                    link1 = encurtarLink(x.a['href'])
                if titulo1 not in repetido and link1 not in repetido:
                    repetido.append(link1)
                    repetido.append(titulo1)
                    print('''{}\nReportagem: {}\n{:.<90}{}'''.format('=' * 100 ,contagem,titulo1, link1))
                    contagem += 1
                else:
                    print()
                try:
                    for y in x.select(tagSub):
                        titulo2 = y.a.text.strip()[:tamanhoString-16]
                        if origem != '':
                            link2 = encurtarLink(y.a['href'], origem)
                        else:
                            link2 = encurtarLink(y.a['href'])
                        if titulo2 not in repetido and link2 not in repetido:
                            repetido.append(titulo2)
                            repetido.append(link2)
                            print('''{:.<90}{}'''.format(titulo2, link2))
                        else:
                            print()
                except:
                    print('')
            print('=' * 100)
            if tagClasse1 != '':
                lerNoticia(site, tagClasse=tagClasse1, tag=tagSub,todoLink=1,contagem=contagem)
        except:
            print("Erro ao ler noticias do site")
    else:
        try:
            for x in sopaSite(site).find_all(tag, {"class",tagClasse}):
                teste = x.select('a')
                for y in teste:
                    titulo3 = y.text.strip()
                    if origem == '':
                        link3 = encurtarLink(y['href'])
                    else:
                        link3 = encurtarLink(y['href'],origem)
                    if titulo3 not in repetido and link3 not in repetido:
                        repetido.append(link3)
                        repetido.append(titulo3)
                        print('''{}\nReportagem: {}\n{:.<90}{}'''.format('=' * 100,contagem,titulo3[:150],link3))
                        contagem += 1
        except :
            print("Erro ao ler noticias do site")
#=============================fim dos leitores de sites
#=============================Menu e execução do programa
def menu():
    print('''
======================================================================
===             {} Notuwiter by: Klayton Bueno Prince              ===
======================================================================
Escolha uma função

1 - Procurar publicações no Twitter
2 - Postar publicação no Twitter
3 - Ver ultimas noticias
8 - Apagar senhas do Sistema
9 - Sair do sistema
======================================================================'''.format(sorriso))

    escolha = input('O quê vamos fazer:')
    if escolha == '1':
        executa('clear')
        oauthTwitter(key_c1, key_c_s1, token_k1, token_k_s1)
        menu()
    elif escolha == '2':
        executa('clear')
        oauthTwitterEscrever(key_c1, key_c_s1, token_k1, token_k_s1)
        menu()
    elif escolha == '3':
        executa("clear")
        noticiasGoogle()
    elif escolha == '8':
        executa("clear")
        try:
            cadastrarSenha()
        except:
            print('Encontramos dificuldades em apagar as senhas do Twitter')
        executa('clear')
        menu()
    elif escolha == '9':
        print("escolheu 9")
        executa('clear && exit')
        menu()
    else:
        executa('clear')
def noticiasGoogle():
    print('''
======================================================================
===                 Lendo noticias de varias fontes                ===
======================================================================
Escolha quais topicos deseja ver as noticias

0- Geral               10- G1                 20- BBC Brasil
1- Brasil              11- Uol                21- BBC Internacional
2- Mundo               12- Terra              22- BBC Economia
3- Negocios            13- R7                 23- BBC Saúde
4- Cien. e Tec.        14- Twitter-hoje       24- BBC Ciência
5- Entretenimento      15- Twitter-noticias   25- BBC Tecnologia
6- Esporte             16- Twitter-esporte    26-
7- Saúde               17- Twitter-entret.    27-
8- Especifica          18- Twitter-divers.    28-
9- EXAME               19-                    29-
================================================================
S+Enter- Sair       
X+Enter- Retornar Menu
Enter  - Apagar itens
================================================================''')
    escolha = input('O quê vamos fazer:')
    if escolha == '0':
        executa('clear')
        lerNoticia(principais, 'NiLAwe', 'h4', total=quantasReportagens(), origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '1':
        executa('clear')
        lerNoticia(brasil,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '2':
        executa('clear')
        lerNoticia(mundo,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '3':
        executa('clear')
        lerNoticia(negocio,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '4':
        executa('clear')
        lerNoticia(citec,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '5':
        executa('clear')
        lerNoticia(entretenimento,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '6':
        executa('clear')
        lerNoticia(esporte,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '7':
        executa('clear')
        lerNoticia(saude,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '8':
        executa('clear')
        pesquisa = urllib.parse.quote(input("O quê vamos pesquisar:"))
        pesquisando = 'news.google.com/search?q=' + pesquisa + '&hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
        lerNoticia(pesquisando,'NiLAwe','h4',total=quantasReportagens(),origem='news.google.com.br/')
        noticiasGoogle()
    elif escolha == '9':
        executa('clear')
        lerNoticia(EXAME,'list-item-title',tag='span',total=quantasReportagens())
        noticiasGoogle()
    elif escolha == '10':
        executa('clear')
        lerNoticia(G1,'feed-post-body','li',total=quantasReportagens())
        noticiasGoogle()
    elif escolha == '11':
        executa('clear')
        lerNoticia(UOL, 'submanchete-col', 'li', total=quantasReportagens())
        #tet(UOL, tagClasse='submanchete-col',tagClasse1='container-cols',total=quantasReportagens())
        noticiasGoogle()
    elif escolha == '12':
        executa('clear')
        lerNoticia(TERRA, 'title',todoLink=1)
        noticiasGoogle()
    elif escolha =='13':
        executa('clear')
        lerNoticia(R7, 'single-trend-title', tag='h3', tagClasse1='single-trend-news-bullets', tagSub='ul')
        noticiasGoogle()
    elif escolha == '14':
        executa('clear')
        lerNoticia(Thoje, "MomentsGuidePage-capsules", todoLink=1)
        noticiasGoogle()
    elif escolha == '15':
        executa('clear')
        lerNoticia(Tnoticia, "MomentsGuidePage-capsules", todoLink=1)
        noticiasGoogle()
    elif escolha == '16':
        executa('clear')
        lerNoticia(Tesporte, "MomentsGuidePage-capsules", todoLink=1)
        noticiasGoogle()
    elif escolha == '17':
        executa('clear')
        lerNoticia(Tentretenimento, "MomentsGuidePage-capsules", todoLink=1)
        noticiasGoogle()
    elif escolha == '18':
        executa('clear')
        lerNoticia(Tdiversao, "MomentsGuidePage-capsules", todoLink=1)
        noticiasGoogle()
    elif escolha == '20':
        executa('clear')
        lerNoticia(BBCbrasil, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()
    elif escolha == '21':
        executa('clear')
        lerNoticia(BBCinternacional, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()
    elif escolha == '22':
        executa('clear')
        lerNoticia(BBCeconomia, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()
    elif escolha == '23':
        executa('clear')
        lerNoticia(BBCsaude, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()
    elif escolha == '24':
        executa('clear')
        lerNoticia(BBCciencia, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()
    elif escolha == '25':
        executa('clear')
        lerNoticia(BBCtecnologia, tagClasse='column--primary', origem='www.bbc.com',todoLink=1)
        noticiasGoogle()

    elif escolha == 'X':
        executa('clear')
        menu()
    elif escolha == 'S':
        executa('clear && exit')
    else:
        executa('clear')
        noticiasGoogle()







menu()
