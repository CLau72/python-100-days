from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Pokemon', 'Type', 'Pokedex Entry']
table.align = "l"
table.add_rows(
    [
    ['Pikachu', 'Electric', 25],
    ['Squirtle', 'Water', 6 ],
    ['Bulbasaur', 'Grass', 1]
    ]
)

print(table)
