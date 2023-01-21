#Reid Witte
#Referencing W3Schools for assistance


def get_combined_dict(dict1, dict2):
    output = {}
    for x in dict1:
        if(dict2.get(x, -1) != -1):
            output.update({x:dict1[x] + dict2[x]})
    return output

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)