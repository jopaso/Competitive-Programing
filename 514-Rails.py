if __name__ == '__main__':
    vagones = int(input())
    while(vagones != 0): 
        lineB = input().split(" ")
        while(int(lineB[0]) != 0):
        
            #print("Salida deseada: ", lineB)
            station = [] #in that stack we will store the cars that are in the station
            lineA = list(range(1, int(vagones) + 1)) #the line with the cars in increasing order
            #print("Entrada: ", lineA)
            posible = True
            for i in lineB:
                #print("Buscando el: ", i)
                #print("Station: ", station, "\nLineA: ", lineA)
                if int(i) in station:
                    if station[len(station) - 1] != int(i): #if its in the station and can't be pop the first it's impossible
                        #print("It's in the stack but not the first")
                        posible = False
                        break
                    else:
                        #print("It's the first in the stack")
                        station.pop() #If the car we are looking for is the first one, we just pop it off the stack
                        continue
                
                j = 0
                while(j < len(lineA)):  #We look for the next car in the lineA
                    if(int(i) == lineA[j]): #if it is the the wanted car we just remove from the list
                        lineA.remove(lineA[j])
                        break
                    else: #if not, we enter the car in the station and remove it from the list
                        station.append(lineA[j])
                        lineA.remove(lineA[j])
            
            if posible:  #We print the answer, Yes or No
                print("Yes")
            else:
                print("No")

            lineB = input().split(" ")

        print()
        vagones = int(input())
