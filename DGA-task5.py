numbers = [4, 5, 2, 1, 5, 2, 5, 3, 8, 5, 6, 2, 1, 6, 2, 6, 8, 88, 88, 2, 5, 3, 2, 7, 4, 6, 4, 5, 6, 2, 5, 6, 3, 7, 3, 7]

# 5 -reqeminin listdəki indekslərini tapın

indexes = [i for i in range(0,len(numbers)) if numbers[i]%5==0]

if __name__ == "__main__":
    print(*indexes, sep = " | ")