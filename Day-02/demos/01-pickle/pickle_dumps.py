import pickle

product = { "id" : 100, "name" : "Pen", "cost" : 12}


filename = 'product.dat'
with open(filename, 'wb') as out_s:
      pickle.dump(product, out_s)

print('saved')