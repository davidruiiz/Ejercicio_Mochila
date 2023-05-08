from mochila import *

if __name__ == '__main__':
    objectos = df_4.values.tolist()
    port_term =[]
    cap_max = 6
    peso_max = 10
    for i in objectos:
        i.append(i[2]/(i[1]))
    objectos.sort(key=lambda x: x[3], reverse=True)
    port_term = mochila_pokemon(objectos, cap_max,peso_max)
    print("La mochila tiene una capacidad de: ", cap_max)
    print(port_term)