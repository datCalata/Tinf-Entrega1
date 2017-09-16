import numpy as np

NUM_V = 3
NUM_C = 5
NUM_N = 3

def print_array(array):
    for item in array:
        print(str(item)+"\n ------- \n")

def print_tables(tables):
    for item in tables:
        print(item)
        print("-------")

def valid_values(values):
    return values[values > 0]

def calc_h(prob):
    val_values = valid_values(prob)
    return np.sum(val_values * np.log2(1/val_values))

def calc_h_list(prob):
    h = 0
    for item in prob:
        h += calc_h(item)
    return h

#Datos del ejercicio, tablas segun enunciado
a = np.array([(1/8, 0, 0), (1/16, 1/64, 1/64), (1/32, 1/16, 1/64), (0, 0, 0), (0, 0, 0)])
e = np.array([(1/8, 0, 0), (1/16, 1/64, 1/64), (0, 0, 0), (1/32, 1/32, 1/32), (0, 1/64, 1/16)])
i = np.array([(0, 0, 0), (0, 0, 0), (1/32, 1/16, 1/64), (1/32, 1/32, 1/32), (0, 1/64, 1/16)])

#DIM TEMPLATE[v, c, n]
list_prob = np.stack((a, e, i))
#Apartado a
val_valid = list_prob[(list_prob>0)]
list_h_conj = val_valid  * np.log2(1/val_valid)
print(list_h_conj)
h_conj = np.sum(list_h_conj)
print(h_conj) #NOTA: DA LO MISMO QUE ANGELA

#Apartado B
#prob nc [c,n]
prob_nc = np.zeros(list_prob.shape[1:3])
for k in range(0,list_prob.shape[0]):
    #print(list_prob[k, 0:, 0:])
    prob_nc += list_prob[k, 0:, 0:]
print("Distribucion Marginal N-C")
print(prob_nc)
#prob nv [v,n]
prob_nv = np.zeros((list_prob.shape[0],list_prob.shape[2]))
for k in range(0,list_prob.shape[1]):
    prob_nv += list_prob[0:, k, 0:]
print("Distribucion Marginal N-V")
print(prob_nv)
#prob cv [v,c]
prob_cv = np.zeros((list_prob.shape[0],list_prob.shape[1]))
for k in range(0,list_prob.shape[2]):
    prob_cv += list_prob[0:,0:,k]
print("Distribucion Marginal C-V")
print(prob_cv)

#Apartado C
h_nc = calc_h(prob_nc)
print("Incertidumbre N-C: "+str(h_nc))

h_nv = calc_h(prob_nv)
print("Incertidumbre N-V: "+str(h_nv))

h_cv = calc_h(prob_cv)
print("Incertidumbre C-V: "+str(h_cv)) #Corregido

#Apartado D
prob_c = np.zeros(list_prob.shape[1])
for v in range(0,list_prob.shape[0]):
    for n in range(0, list_prob.shape[2]):
        prob_c += list_prob[v, 0:, n]
print("Probabilidad marginal P(c)")
print(prob_c)
#print(sum(prob_c))
prob_v = np.zeros(list_prob.shape[0])
for c in range(0,list_prob.shape[1]):
    for n in range(0, list_prob.shape[2]):
        prob_v += list_prob[0:, c, n]
print("Probabilidad marginal P(v)")
print(prob_v)
#print(sum(prob_v))
prob_n = np.zeros(list_prob.shape[2])
for v in range(0,list_prob.shape[0]):
    for c in range(0, list_prob.shape[1]):
        prob_n += list_prob[v, c, 0:]
print("Probabilidad marginal P(n)")
print(prob_n)
#print(sum(prob_n))

#Apartado E
h_c = calc_h(prob_c)
h_v = calc_h(prob_v)
h_n = calc_h(prob_n)
print('Incertidumbre de V: {0} \nIncertidumbre de C: {1} \nIncertidumbre de N: {2} \n '.format(h_v, h_c, h_n))

#Apartado F
'''
c = x|  1   2   3
a
e
i 
'''
list_prob_nv_c = []
for c in range(0,list_prob.shape[1]):
    list_prob_nv_c.append(list_prob[0:,c,0:]/prob_c[c])
print("Distribucion de probabilidad P(n,v | c)")
print_tables(list_prob_nv_c)

#Apartado G
h_nv_c = h_conj - h_c
print("La Incertidumbre condicional H(C,V|N) :{0}".format(h_nv_c))

#Apartado H
'''
n = x|  b d f l m
a
e
i 
'''
print("Distribucion de probabilidad P(c,v | N)")
list_prob_cv_n= []
for c in range(0, list_prob.shape[2]):
    list_prob_cv_n.append(list_prob[0:,0:,n]/prob_n[n])
print("Distribucion de probabilidad P(n,v | c)")
print_tables(list_prob_cv_n)
#Apartado I
h_cv_n = h_conj - h_n
print("La Incertidumbre condicional H(C,V|N) {0}".format(h_cv_n))

#Apartado J
h_cv_n2 = h_conj - h_n
print("La Incertidumbre condicional H(C,V|N) {0}".format(h_cv_n2))

#Apartado k
print("Apartado K")
h_n_c_v = h_conj - h_cv
h_c_n_v = h_conj - h_nv
h_v_n_c = h_conj - h_nc
print("La Incertidumbre condicional H(N | C, V): {0} \nLa Incertidumbre condicional H( C | N, V) es: {1} \nLa Incertidumbre condicional H(V | N, C) es: {2} \n".format(h_n_c_v,h_c_n_v,h_v_n_c))

#Apartado l
print("Apartado L")
i_n_c = h_c - (h_nc - h_n)
i_n_v = h_v - (h_nv - h_n)
i_c_v = h_v - (h_cv - h_c)
print("La informacion mutua I(N;C): {0}".format(i_n_c))
print("La informacion mutua I(N;V): {0}".format(i_n_v))
print("La informacion mutua I(C;V): {0}".format(i_c_v))

#Apartado m
print("Apartado M")
i_n_c_v = h_nv - h_v - h_n_c_v
i_n_v_c = h_nc - h_c - h_n_c_v
i_c_v_n = h_nc - h_n - h_c_n_v
print("La informacion mutua I(N;C/V): {0}".format(i_n_c_v))
print("La informacion mutua I(N;V/C): {0}".format(i_n_v_c))
print("La informacion mutua I(C;V/N): {0}".format(i_n_c_v))
