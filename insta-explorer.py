import instagram_explore as ie

# Busca informações do perfil desejado #
# Retorna informções do perfil, posts, biografia, legendas e etc #
# Retorno é em formato JSON #
result = ie.user('pycodebr')

# Mostra resultados retornados #
print(result.data)