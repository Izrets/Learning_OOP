# dictionaryname key = value

for i in range(len(lst_in)):
    lst_data.append({})

flatten_lst_in = []
sp_lst_in = [i.split() for i in lst_in]

for i in sp_lst_in:
    flatten_lst_in += i
lst_in = flatten_lst_in

lst_in_id = 0

for i in lst_data:
    for j in FIELDS:
        i[j] = lst_in[lst_in_id]
        lst_in_id +=1


# [{'id': None, 'name': None, 'old': None, 'salary': None}, {'id': None, 'name': None, 'old': None, 'salary': None}]
#
# for i in lst_in_sp:
#     for j in i:
