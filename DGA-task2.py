my_list = [4, 5, 2, 1, 5, 2, 5, 3, 5, 6, 2, 1, 6, 2, 6, 2, 5, 3, 2, 7, 4, 6, 4, 5, 6, 2, 5, 6, 3, 7, 3, 7]

# my_list icərisində istənilən elementin sayını qaytaran funksiya yazmalıyıq

def CountOfElement(_search,_list):
    return my_list.count(_search)

def count_of_element(_search,_list):
    _list = [element for element in _list if element == _search]
    return len(_list)
    
def countOfElement(_search,_list):
    count = 0
    for element in _list:
        if(element==_search): count+=1
    return count 

if __name__ == "__main__":
    # listlərin count metodundan istifadə edərək :
    print(CountOfElement.__name__)
    print(CountOfElement(5,my_list))   # 7
    print(CountOfElement(4,my_list))   # 3
    print(CountOfElement(6,my_list))   # 6
    print(CountOfElement(100,my_list)) # 0
    # listlərin count metodundan istifadə etmədən (len metodu + list comprehension ile):
    print(count_of_element.__name__)
    print(count_of_element(5,my_list))   # 7
    print(count_of_element(4,my_list))   # 3
    print(count_of_element(6,my_list))   # 6
    print(count_of_element(100,my_list)) # 0
    # hər şey 'custom'
    print(countOfElement.__name__)    
    print(countOfElement(5,my_list))   # 7
    print(countOfElement(4,my_list))   # 3
    print(countOfElement(6,my_list))   # 6
    print(countOfElement(100,my_list)) # 0
