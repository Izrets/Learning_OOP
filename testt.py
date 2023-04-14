# dictionaryname key = value
FIELDS = ('id', 'name', 'old', 'salary')
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
lst_in2 = [k.split() for k in lst_in]
# lst_in2 = ['1', 'Сергей', '35', '120000']
lst_data_a = list(zip(FIELDS, lst_in2))
lst_data = {x: y for x, y in lst_data_a}
print(lst_data)
