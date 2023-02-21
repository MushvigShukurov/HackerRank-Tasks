numbers = [4, 5, 2, 1, 5, 2, 5, 3, 8, 5, 6, 2, 1, 6, 2, 6, 8, 88, 88, 2, 5, 3, 2, 7, 4, 6, 4, 5, 6, 2, 5, 6, 3, 7, 3, 7]

# listdəki ilk 6-ya bölünən ədədi və indeksini tapın

numbers_2 = [num for num in numbers if num%6==0]


if __name__ == "__main__":
    print(numbers_2[0], numbers.index(numbers_2[0]))