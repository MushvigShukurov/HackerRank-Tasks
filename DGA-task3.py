numbers = [4, 5, 2, 1, 5, 2, 5, 3, 8, 5, 6, 2, 1, 6, 2, 6, 8, 88, 88, 2, 5, 3, 2, 7, 4, 6, 4, 5, 6, 2, 5, 6, 3, 7, 3, 7]

# numbers -listindəki elementlərdən təkrarlanan elementləri artan sırada düzün (unique olsun)

numbers = set([num for num in numbers if numbers.count(num)>1])

if __name__ == "__main__":
    print(*numbers,sep=" | ")