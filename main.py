import sys  # para poder usar os argumentos e usar diretamente pelo terminal

import requests  # necessário instalar com o pip install requests


def brute(url, wordlist):  # colocando tudo dentro de uma função
    # agora o laço que vai pegar cada item da lista para fazer o brute force
    for word in wordlist:
        try:
            # crie a resposta para a requisição
            url_final = f"http://{url}/{word.strip()}"  # .strip() ignora o pular de linha do arquivo
            resposta = requests.get(url_final)
            code = resposta.status_code
            if code != 404:
                # como só precisamos saber se o diretório existe ou não usamos o status_code que quando der 200 quer dizer
                # que existe
                print(url_final, "=", resposta.status_code)
        except KeyboardInterrupt:  # no caso apertando Ctrl+C para parar o programa
            sys.exit(0)
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    args = sys.argv  # instanciando o objeto argv para poder usar os argumentos

    # determinando o primeiro argumento
    url = args[1]  # URL usada para brute force
    wordlist = args[2]  # lista dos diretórios para brute force

    # abrir o arquivo da wordlist que será usado no brute force
    with open(wordlist, "r") as file:  # pode-se usar o caminho completo "/usr/share/dirb/wordlists/small.txt"
        wordlist = file.readlines()  # readlines para separar linha por linha
        brute(url, wordlist)

