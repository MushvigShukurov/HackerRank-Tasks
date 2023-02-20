my_list = ["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]

# Gözlənilən nəticə :
"""
my_list = [
    ["Yanvar","Fevral",["Mart",["Aprel"]]],
    ["May","Iyun",["Iyul","Avgust"]],
    ["Sentyabr","Oktyabr",["Noyabr",["Dekabr"]]]
]
"""

if __name__ == "__main__":
    for step in range(int(len(my_list) / 4)):
        group = my_list[0:4]
        [a,b,c,d] = group
        if(step==1):        
            my_list.append([a,b,[c,d]])
        else:
            my_list.append([a,b,[c,[d]]])
        my_list = my_list[4:]
    for new_list in my_list:
        print(new_list)