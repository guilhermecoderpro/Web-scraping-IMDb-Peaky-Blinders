#!/usr/bin/env python
# coding: utf-8

# ## Análise dos Dados da Série "Peaky Blinders"
# #### Os dados foram retirados do site IMDB e podem ser acessados no link: https://www.imdb.com/title/tt2442560/

# In[3]:


from bs4 import BeautifulSoup as bs
import requests as rq


# In[4]:


url = 'https://www.imdb.com/title/tt2442560/'
r = rq.get(url)
print(r)


# In[5]:


soup = bs(r.content, 'html.parser')


# In[6]:


type(soup)


# In[7]:


#Nome da Série
nome_da_serie = soup.find('h1').text
print(nome_da_serie)


# In[8]:


#Ano de Lançamento da Série
ano_de_lancamento = soup.find('span', class_ = 'TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex').text
ano_de_lancamento


# In[25]:


#Avaliação do IMDb
avaliacao = soup.find('span', class_ = 'AggregateRatingButton__RatingScore-sc-1il8omz-1 fhMjqK').text
avaliacao2 = print(avaliacao + '/10')


# In[10]:


#Popularidade no Ranking da IMDb Atualmente
pop = soup.find('div', class_ = 'TrendingButton__TrendingScore-rbd4o3-1 CRmBe').text
print(pop)


# In[11]:


#Quantos pontos a série caiu no Ranking da IMDb?
lost_points = soup.find('div', class_ = 'TrendingButton__TrendingDelta-rbd4o3-2 cZhqd').text
lost_points


# In[12]:


#Em que posição se encontrava a série antes da perda de pontos?
last_position = int(pop) - int(lost_points)
last_position


# In[13]:


#Sinopse
sinopse = soup.find('div', class_ = 'GenresAndPlot__TextContainerBreakpointXS-cum89p-0 GxFuV').text
print(sinopse)


# ### Análise dos dados encontrados

# ##### Quando a série foi lançada?

# In[87]:


#Lembrete da função Replace: variável + .replace('primeiro nome,', 'novo nome,')

ano = ano_de_lancamento.replace('2013–', '2013')
print('A série foi lançada no ano de', ano)


# ##### Qual era o nível inicial ocupado pela série no ranking da IMDb ?

# In[118]:


print('O nível/posição anteriormente ocupado(a) pela série era o', last_position)


# ##### Qual a posição atual da série no ranking do site IMDb?

# In[117]:


print('O nível/posição atual ocupado(a) pela série é o', pop)


# ##### Do que se trata a série?

# Trata-se de um épico familiar de gângsteres ambientado na Inglaterra de 1900, que se concentra em uma 
# gangue e seu chefe , Thomas Shelby. A gangue da família Shelby era famosa por sua influência na Inglaterra e também pelo costume de costurar lâminas de barbear nas pontas de seus bonés.

# In[32]:


#### Qual a avaliação da série no site?
print('A série recebeu uma avaliação bem positiva:', avaliacao, 'pontos em 10')

