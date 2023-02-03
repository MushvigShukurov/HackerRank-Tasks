from string import ascii_lowercase
def print_rangoli(size):
    width = size + (size-1)
    width += (width-1)
    empty_list = []
    num = size
    
    our_string = ascii_lowercase
    center_string = ""
    prev = ""
    if size>0 and size < 27:
        size -= 1
        for _ in range(num):
            center_string += our_string[size]
            size -= 1
            result = "-".join(list(center_string+prev[::-1]))
            empty_list.append(result.center(width,"-"))
            prev = center_string
        index = ((num*2)-1) - len(empty_list) - 1
        while len(empty_list) < ((num*2)-1):
            empty_list.append(empty_list[index])
            index-=1
        for element in empty_list:
            print(element)
    else: return False
    