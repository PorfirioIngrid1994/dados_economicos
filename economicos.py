import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

gapminder = px.data.gapminder()
df = px.data.gapminder().query('country == "Brazil"').set_index('year')

print(df.head())

plt.plot(df.index, df['gdpPercap'])
plt.title('PIB per capita do Brasil')
plt.ylabel('PIB per capita')
plt.xlabel('Tempo')

# Relação entre expectativa de vida e renda per capita no Brasil:

plt.figure(figsize=(12, 4))
plt.scatter(df['lifeExp'], df['gdpPercap'])
plt.xlabel('Expectativa de vida')
plt.ylabel('Renda Per Capita')
plt.title('Relação entre Expectativa de Vida e Renda Per Capita no Brasil')
plt.show()

plt.bar(x=df.index, height=df['pop'], color='red')
plt.title('População Brasileira')
plt.show()

# Filtrar continente

def filtrar_continente(continente):
    df = px.data.gapminder()
    df = df[df['continent'] == continente]
    return df

# Filtrar continente

def filtrar_pais(pais, variavel):
    df = px.data.gapminder()
    df = df[df['country'] == pais][variavel]
    return df

americas = filtrar_continente('Americas')
paises = americas['country'].unique()
plt.figure(figsize=(12, 8))

for pais in paises:
    plt.scatter(filtrar_pais(pais=pais, variavel='lifeExp'),
                filtrar_pais(pais=pais, variavel='gdpPercap'))
    
plt.legend(labels=paises, loc='best')
plt.title('Relação entre renda per capita e expectativa de vida', loc='left')
plt.xlabel('Expectativa de vida')
plt.ylabel('Renda per capita')
plt.show()
