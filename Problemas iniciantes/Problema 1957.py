def int_hex(v):
    v = hex(v)
    v = v[2:]
    return v

def main(v):
    v = v.upper()
    print(v)

main(int_hex(int(input())))

#https://github.com/brenonf/URI-python-3/blob/master/1957.py
