import yaml 

f = open('recipe.yaml', 'r')
yml=f.read()
new_txt= open('recipes.txt', 'w')
new_txt.write(yml)
print(yml)
