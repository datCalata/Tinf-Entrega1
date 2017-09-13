import numpy as np

def print_array(array):
    for item in array:
        print(str(item)+"\n ------- \n")

def valid_values(values):
    return values[values > 0]

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
val_nc = valid_values(prob_nc)
h_nc = np.sum(val_nc*np.log2(1/val_nc))
print("Incertidumbre N-C: "+str(h_nc))


val_nv = valid_values(prob_nv)
h_nv = np.sum(val_nv*np.log2(1/val_nv))
print("Incertidumbre N-V: "+str(h_nv))

val_cv = prob_cv[prob_cv > 0]
h_cv = np.sum(val_cv*np.log2(1/val_cv))
print("Incertidumbre C-V: "+str(h_cv)) #Error angela


