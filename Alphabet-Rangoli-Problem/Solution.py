def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase
    #print(alpha)
    new_list = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        new_list.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(new_list[:0:-1]+new_list))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
