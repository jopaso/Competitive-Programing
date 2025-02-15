import re


def check_inside(pos, lines):
	if (pos[0] >= 0 and pos[0] < len(lines)) and (pos[1] >= 0 and pos[1] < len(lines[0])):
		return True
	return False

def main(lines):
	dict = {}
	for i,line in enumerate(lines):
		for j, letter in enumerate(line):
			if re.match("[a-zA-Z0-9]", letter):
				if letter in dict:
					dict[letter].append((i, j))
				else:
					dict[letter] = [(i, j)]
	print(dict)
	antinodes = []
	for key in dict.keys():
		antenas = dict[key]
		for i in range(len(antenas)-1):
			for j in range(i+1, len(antenas)):
				diff_i = antenas[j][0] - antenas[i][0]
				diff_j = antenas[i][1] - antenas[j][1]
				
				k = 0
				ant_pos_up = ((antenas[i][0] - k*diff_i), (antenas[i][1] + k*diff_j))
				ant_pos_down = ((antenas[j][0] + k*diff_i), (antenas[j][1] - k*diff_j))
				while check_inside(ant_pos_up, lines):
					print(f'Antinode in {ant_pos_up}')
					antinodes.append(ant_pos_up)
					k += 1
					ant_pos_up = ((antenas[i][0] - k*diff_i), (antenas[i][1] + k*diff_j))

				k = 0
				while check_inside(ant_pos_down, lines): 
					print(f'Antinode in {ant_pos_down}')
					antinodes.append(ant_pos_down)
					k += 1
					ant_pos_down = ((antenas[j][0] + k*diff_i), (antenas[j][1] - k*diff_j))
					
					
#	for line in lines:
#		print(''.join(line))

	print(f'TOTAL ANTINODES: {len(set(antinodes))}')

if __name__ == '__main__':
	with open('input.in', 'r') as f:
		arr = []
		for line in f.readlines():
			arr.append(list(line.strip()))
		main(arr)
