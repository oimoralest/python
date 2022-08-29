tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}
print(tables)

# Write your code below:
def assign_table(table_number, name, vip_status=False):
    tables[table_number] = [name, vip_status]

# Using positional arguments
assign_table(6, 'Yoni', False)
print(tables)

# Using keyword arguments
assign_table(name='Martha', table_number=3, vip_status=True)
print(tables)

# Using default values
assign_table(4, 'Karla')
print(tables)
