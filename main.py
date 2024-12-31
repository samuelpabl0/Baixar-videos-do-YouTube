# Importa a classe YouTube do módulo pytube
from pytube import YouTube

# Solicita ao usuário que insira o link do vídeo que deseja baixar
link = input("Digite o Link do Vídeo que Deseja Baixar:")

# Cria uma instância da classe YouTube, passando o link do vídeo como argumento
yt = YouTube(link)

# Imprime o título do vídeo que está sendo baixado
print("Baixando", yt.title)

# Filtra as diferentes resoluções disponíveis para o vídeo
resolucao = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

# Faz o download do vídeo na resolução selecionada
resolucao.download()

# Indica que o download foi concluído
print("Download Concluído!")
