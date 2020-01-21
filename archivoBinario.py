import pickle

#milista = ['jose','juan','julian','judith','julia','jazmin']

#milistabinario = open('listabinario','wb')

#pickle.dump(milista,milistabinario)

#milistabinario.close()

fichero = open('listabinario','rb')

archivob = pickle.load(fichero)
fichero.close()
print(archivob)
