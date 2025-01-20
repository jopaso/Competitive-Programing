


def compute_checksum(final_block):
	checksum = 0
	joint_block = ""
	for block in final_block:
		for val in block:
			joint_block += str(val)
		

	for i, num in enumerate(joint_block):
		if num != '.':
			checksum += (i * int(num))

	print(joint_block)
	return checksum

def format_blocks(disk):

	blocks = []
	actual_id = 0

	for i,letter in enumerate(disk):
		if i % 2 == 0:
			blocks.append([actual_id] * int(letter))
			actual_id += 1
		else:
			blocks.append(['.'] * int(letter))

	return blocks

def find_fitting_block(blocks, act_block):
	for i, block in enumerate(blocks):
		if '.' in block and len(block) >= len(act_block):
			return i, block
	return None, None

def main(disk):
	blocks = format_blocks(disk)

	used_blocks = [inner_list for inner_list in blocks if inner_list] #Remove empty blocks
	#print(used_blocks)
	
	#Move blocks
	for i in range(len(used_blocks)-1, -1, -1):
		block = used_blocks[i]
		##print(f"Checking block {block}")
		if not '.' in block:
			pos, fitting_block = find_fitting_block(used_blocks, block)

			if pos and pos < i: # Switch block
				##print(f'Fitting block: {block} in pos {pos}:{fitting_block}')
				
				#send '.' to back
				if (i-1 >= 0 and '.' in used_blocks[i-1]) and (i+1 < len(used_blocks) and '.' in used_blocks[i+1]):
					used_blocks[i-1] += used_blocks[i+1]
					del used_blocks[i+1]
					used_blocks[i-1] += ['.'] * len(block)
					del used_blocks[i]

				elif i-1 >=0 and '.' in used_blocks[i-1]:
					used_blocks[i-1] += ['.'] * len(block)
					del used_blocks[i]

				elif i+1 < len(used_blocks) and '.' in used_blocks[i+1]:
					used_blocks[i+1] += ['.'] * len(block)
					del used_blocks[i]
				
				else:
					used_blocks[i] = ['.'] * len(block)
				
				#send block to front
				used_blocks[pos] = block
				dif = len(fitting_block) - len(block)
				if dif > 0:
					if '.' in used_blocks[pos+1]:
						#print("SIII")
						used_blocks[pos+1] += ['.'] * dif	
					else:
						#print("JOoo")
						used_blocks.insert(pos+1, ['.'] * dif)
				##print(f'Actual look of used Blocks: \n{used_blocks}')



	final_check = [inner_list for inner_list in used_blocks if inner_list] #Remove empty blocks
	#print(final_check)

	print(f'\n\nFINAL CHECKSUM: {compute_checksum(final_check)}')


if __name__ == '__main__':
	disk = ""
	with open('input.in', 'r') as f:
		disk = f.readline()
	
	main(disk.strip())
	
