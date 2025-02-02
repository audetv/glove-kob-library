from razdel import tokenize

tokens = list(tokenize('Кружка-термос на 0.5л (50/64 см³, 516;...)'))
# print(tokens)

 
print([_.text for _ in tokens])
