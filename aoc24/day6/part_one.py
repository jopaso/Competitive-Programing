


def main():
	lines = []
	with open('input.in', 'r') as f:
		lines = f.readlines()

	gpos = ()
	arlines = []
	for i,line in enumerate(lines):
		arlines.append(list(line.strip()))
		if '^' in line:
			ind = line.index('^')
			gpos = (i, ind)

	
	print(f'INITIAL GPOS: {gpos}')
	places_vis = move_guard(arlines, gpos, 'up')
	print(f'\nVISITED: {places_vis}')

def move_guard(lines, gpos, gdir):
	visited = 0
	fin = False
	while not fin:
		match gdir:
			case 'right':
				print(f"Going right\tGPOS:{gpos}")
				for j in range(gpos[1], len(lines)):
					# print(f'POS: ({gpos[0]}, {j}')
					if not lines[gpos[0]][j] == 'X':
						visited += 1
						lines[gpos[0]][j] = 'X'

					if j == len(lines) - 1: #Is leaving
						gdir = 'LEAVE'
					
					elif lines[gpos[0]][j+1] == '#': #turns down
						gdir = 'down'
						gpos = (gpos[0], j)
						break

			case 'left':
				print(f"Going left\tGPOS:{gpos}")
				for j in range(gpos[1], -1, -1):
					# print(f'POS: ({gpos[0]}, {j}')
					if not lines[gpos[0]][j] == 'X':
						visited += 1
						lines[gpos[0]][j] = 'X'

					if j == 0: #Is leaving
						gdir = 'LEAVE'
					
					elif lines[gpos[0]][j-1] == '#': #turns up
						gdir = 'up'
						gpos = (gpos[0], j)
						break
				

			case 'up':
				print(f"Going up\tGPOS:{gpos}")
				for i in range(gpos[0], -1, -1):
					# print(f'POS: ({i}, {gpos[1]}')
					if not lines[i][gpos[1]] == 'X':
						visited += 1
						lines[i][gpos[1]] = 'X'
					if i == 0: #Is leaving
						gdir = 'LEAVE'
					
					elif lines[i-1][gpos[1]] == '#': #turns right
						gdir = 'right'
						gpos = (i, gpos[1])
						break
			case 'down':
				print(f"Going down\tGPOS:{gpos}\tvisited: {visited}")
				for i in range(gpos[0], len(lines[0])):

					if not lines[i][gpos[1]] == 'X':
						visited += 1
						lines[i][gpos[1]] = 'X'
					if i == len(lines[0]) - 1: #Is leaving
						gdir = 'LEAVE'
					
					elif lines[i+1][gpos[1]] == '#': #turns left
						gdir = 'left'
						gpos = (i, gpos[1])
						break
			case _: #Leaves
				print("LEAVING")
				fin = True

	for line in lines:
		print("".join(line))
	return visited


if __name__ == '__main__':
	main()
