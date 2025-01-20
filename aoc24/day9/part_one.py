


def compute_checksum(final_block):
	checksum = 0
	for i, num in enumerate(final_block):
		checksum += (i * int(num))
	return checksum

def main(disk):
	blocks = []
	act_id = 0
	blocs_idd = [] #Blocks without '.'
	for i,letter in enumerate(disk):
		if i % 2 == 0:
			blocs_idd += ([act_id] * int(letter))
			blocks += ([act_id] * int(letter))
			act_id += 1
		else:
			blocks += (['.'] * int(letter))

	print(blocks)
	print(blocs_idd)
	blocs_idd = blocs_idd[::-1]
	final_check = []
	for block in blocks:
		if (len(blocs_idd) < 1):
			break
		if block == '.':
			final_check += [blocs_idd[0]]
			del blocs_idd[0]
		
		else:
			final_check += [block]
			del blocs_idd[-1]
		

	print(f'FINAL CHECKSUM: {compute_checksum(final_check)}')


if __name__ == '__main__':
	disk = ""
	with open('input.in', 'r') as f:
		disk = f.readline()
	
	main(disk.strip())
	
