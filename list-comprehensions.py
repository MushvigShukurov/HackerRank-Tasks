def custom_perm(x,y,z,n):
    empty_list = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if sum([a,b,c])!=n]
    # empty_list = []
    # for a in range(x+1):
    #     for b in range(y+1):
    #         for c in range(z+1):
    #             if a + b + c != n:
    #                 empty_list.append([a,b,c])
    return empty_list



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(custom_perm(x,y,z,n))