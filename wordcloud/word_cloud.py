from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Carregando a lista de palavras
arquivo = open('palavras.txt','r')
palavras = arquivo.read()
arquivo.close()

# Criação da Word-cloud
word_cloud = WordCloud(width=600, height=400, max_words=200,background_color='white',max_font_size=30).generate(palavras)

# Configurar Visualização
plt.figure(figsize=[8,8])
plt.imshow(word_cloud, cmap='Accent')
plt.axis('off')


# Salvar Imagem
plt.savefig('words.png')

# Visualizar
plt.show()