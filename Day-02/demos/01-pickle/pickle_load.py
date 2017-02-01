import pickle
filename = 'product.dat'
with open(filename, 'r') as in_s:
      product = pickle.load(in_s)
      print(product)
