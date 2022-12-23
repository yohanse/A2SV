def swap_case(s):
    res=""
    for i in s:
        if i==i.lower():
            res += i.upper()
        else:
            res += i.lower()
            
    return res

if __name__ == '__main__':