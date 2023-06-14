from prettytable import prettyTable
table = prettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"
print(table)
