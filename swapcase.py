def swap_case(s):
    res=""
    for i in s:
        res+=(i.lower() if i==i.upper() else i.upper())       
    return res

if __name__ == '__main__':