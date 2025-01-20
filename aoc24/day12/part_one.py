import sys
def compute_fences(farm, plant, i, j):

    fences = 0
    if i == 0 or i > 0 and farm[i-1][j] != plant:
        fences+= 1
    if j == 0 or j > 0 and farm[i][j-1] != plant:
        fences+= 1
    if i == len(farm) -1 or i < len(farm) - 1 and farm[i+1][j] != plant:
        fences+= 1
    if j == len(farm[i]) -1 or j < len(farm[i]) - 1 and farm[i][j+1] != plant:
        fences+= 1

    return fences

def compute_area(farm, plant, i, j, visited_plants):
    #print(f'Visiting {(i, j)} -> {farm[i][j]} for plant {plant}')
    visited_plants[i][j] = True
    fences = compute_fences(farm, plant, i, j)
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
            new_ar, new_fence = compute_area(farm, plant, pos[0], pos[1], visited_plants)
            area += new_ar
            fences += new_fence

    return area, fences

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
                area, fences = compute_area(farm, plant, i, j, visited_plants)
                print(f'Plant {plant} starting in {(i, j)} has area of {area} and {fences} fences')
                cost += area*fences
    
    print(f"Total cost: {cost}")

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    
    farm = []
    for li in lines:
        farm.append(li.strip())
    main(farm)