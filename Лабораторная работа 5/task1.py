from pprint import pprint


list_ = [{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(16)]
pprint(list_)
