#IMPORTANTE!!!!  todos los casos de prueba funcionan pero UVA da time limit exceeded :'(
cases = int(input())
input() #The  first blank line

while cases > 0:
    #print("cases: ", cases)
    
    counter = 0
    tree = input() #the name of the tree
    dictionary = {} #we will store the tree and how many times it appears here
    while(tree != "exit() and tree): #while there is no blank line
        #print("Tree name: ", tree)
        counter += 1
        if dictionary.get(tree) == None:
            dictionary[tree] = 1
            #print("valor añadido al diccionatio")
        else:
            dictionary[tree] += 1
            #print("valor modificado al diccionatio")
        try:
            tree = input()
        except:
            break
    
    keys = list(dictionary)
    keys.sort()
    #print("contador: ", counter)
    for k in keys:
        print (k, "{0:.4f}".format((dictionary.get(k) / counter) * 100, 4))
    cases -= 1
    if cases != 0:
        print()



