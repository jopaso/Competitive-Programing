import sys
from collections import deque


def compute_fences(farm, plant, i, j):

    fences = 0
    fences_arr = []
    if i == 0 or i > 0 and farm[i-1][j] != plant:
        fences+= 1
        fences_arr.append([(i-0.5, j), (-1, 0)])
    if j == 0 or j > 0 and farm[i][j-1] != plant:
        fences+= 1
        fences_arr.append([(i, j-0.5), (0, -1)])
    if i == len(farm) -1 or i < len(farm) - 1 and farm[i+1][j] != plant:
        fences+= 1
        fences_arr.append([(i+0.5, j), (1,0)])
    if j == len(farm[i]) -1 or j < len(farm[i]) - 1 and farm[i][j+1] != plant:
        fences_arr.append([(i, j+0.5), (0, 1)])
        fences+= 1

    return fences, fences_arr

def compute_area(farm, plant, i, j, visited_plants):
    #print(f'Visiting {(i, j)} -> {farm[i][j]} for plant {plant}')
    visited_plants[i][j] = True
    fences, fenc_arr = compute_fences(farm, plant, i, j)
    area = 1
    queue = []
    #queue possible movements
    if i > 0 and farm[i-1][j] == plant:
        queue.append((i-1, j))
    if j > 0 and farm[i][j-1] == plant:
        queue.append((i, j-1))
    if i < len(farm) - 1 and farm[i+1][j] == plant:
        queue.append((i+1, j))
    if j < len(farm[i]) - 1 and farm[i][j+1] == plant:
        queue.append((i, j+1))

    while queue:
        pos = queue.pop()
        if not visited_plants[pos[0]][pos[1]]:
            new_ar, new_fence, new_fence_arr = compute_area(farm, plant, pos[0], pos[1], visited_plants)
            area += new_ar
            fences += new_fence
            fenc_arr += new_fence_arr

    return area, fences, fenc_arr

def compute_sides(fence_arr):
    fence_deque = deque(fence_arr)
    sides = 0
    final_sides = []
    while(fence_deque):
        fence = fence_deque.popleft()
        check = fence[0]
        direction = fence[1]
        final_sides.append(check)
        sides += 1
        elm = False

        try:
            str(check[0]).index('.') # Will raise an error if there is no '.' -> the '.' is in check[1] 
            # Check to the right
            i = 1
            aux = (check[0], check[1] + i)
            while [aux, direction] in fence_deque:
                elm = True
                fence_deque.remove([aux, direction])
                i += 1
                aux = (check[0], check[1] + i)

            # Check to the left
            i = 1
            aux = (check[0], check[1] - i)
            while [aux, direction] in fence_deque:
                elm = True
                fence_deque.remove([aux, direction])
                i += 1
                aux = (check[0], check[1] - i)
        except:
        
            # Check up
            i = 1
            aux = (check[0] - i, check[1])
            while [aux, direction] in fence_deque:
                fence_deque.remove([aux, direction])
                i += 1
                aux = (check[0] - i, check[1])
            
            # Check down
            i = 1
            aux = (check[0] + i, check[1])
            while [aux, direction] in fence_deque:
                fence_deque.remove([aux, direction])
                i += 1
                aux = (check[0] + i, check[1])

    print(final_sides)
    return sides
def main(farm):
    #Search area
    visited_plants = []
    for i in range(len(farm)):
        row = []
        for j in range(len(farm[0])):
            row.append(False)
        
        visited_plants.append(row)
    cost = 0

    for i, row in enumerate(farm):
        for j, plant in enumerate(row):
            if not visited_plants[i][j]:
                area, fences, fence_array = compute_area(farm, plant, i, j, visited_plants)
                sides = compute_sides(fence_array)
                print(f'\nPlant {plant} starting in {(i, j)} has area of {area}, {fences} fences and {sides} sides ---> {sides*area}€\n')
                cost += sides*area
    
    print(f"Total cost: {cost}")

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    
    farm = []
    for li in lines:
        farm.append(li.strip())
    main(farm)