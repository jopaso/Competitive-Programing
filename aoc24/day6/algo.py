import threading

class SearchingThread(threading.Thread):
	def __init__(self, lines, init, fin, gpos, lock, shared_val):
		super().__init__()
		self.lines = lines
		self.init = init
		self.fin = fin
		self.gpos = gpos
		self.lock = lock
		self.shared_val = shared_val

	def run(self):
		tmp_val = self.brute_force(self.lines, self.gpos, self.init, self.fin)

		print(f'Found obstacles: {tmp_val}')
		with self.lock:
			self.shared_val["val"] += tmp_val



	def brute_force(self, lines, gpos, init, fin):
		obst = 0
		length = (fin - init - 1, len(lines[0]))
		for i in range (init, fin):
			line = lines[i]
			for j, val in enumerate(line):
				if val == '#' or val == '^':
					continue
				new_arr = []
				for l in lines:
					new_arr.append(l.copy())
				new_arr[i][j] = '#' 
				
				if self.move_guard(new_arr, (gpos[0], gpos[1]), 'up'):
					print(f"BUCLE in {i},{j}\n")
					obst += 1
		return obst

	def move_guard(self, lines, gpos, gdir):
		directions = []
		fin = False
		while not fin:
			match gdir:
				case 'right':
					#print(f"Going right\tGPOS:{gpos}")
					for j in range(gpos[1], len(lines)):
						
						dict_entry = [(gpos[0], j), gdir]
						if dict_entry in directions:
							return True
						else:
							directions.append(dict_entry)

						if not lines[gpos[0]][j] == 'X':
							lines[gpos[0]][j] = 'X'

						if j == len(lines) - 1: #Is leaving
							gdir = 'LEAVE'
						
						elif lines[gpos[0]][j+1] == '#': #turns down
							gdir = 'down'
							gpos = (gpos[0], j)
							break
				case 'left':
					# print(f"Going left\tGPOS:{gpos}")
					for j in range(gpos[1], -1, -1):
						# print(f'POS: ({gpos[0]}, {j}')
						dict_entry = [(gpos[0], j), gdir]
						if dict_entry in directions:
							return True
						else:
							directions.append(dict_entry)

						if not lines[gpos[0]][j] == 'X':
							lines[gpos[0]][j] = 'X'

						if j == 0: #Is leaving
							gdir = 'LEAVE'
						
						elif lines[gpos[0]][j-1] == '#': #turns up
							gdir = 'up'
							gpos = (gpos[0], j)
							break
				case 'up':
					# print(f"Going up\tGPOS:{gpos}")
					for i in range(gpos[0], -1, -1):
						# print(f'POS: ({i}, {gpos[1]}')
						dict_entry = [(i, gpos[1]), gdir]
						if dict_entry in directions:
							return True
						else:
							directions.append(dict_entry)

						if not lines[i][gpos[1]] == 'X':
							lines[i][gpos[1]] = 'X'
						if i == 0: #Is leaving
							gdir = 'LEAVE'
						
						elif lines[i-1][gpos[1]] == '#': #turns right
							gdir = 'right'
							gpos = (i, gpos[1])
							break
				case 'down':
					# print(f"Going down\tGPOS:{gpos}\tvisited: {visited}")
					for i in range(gpos[0], len(lines[0])):
						dict_entry = [(i, gpos[1]), gdir]
						if dict_entry in directions:
							return True
						else:
							directions.append(dict_entry)

						if not lines[i][gpos[1]] == 'X':
							lines[i][gpos[1]] = 'X'
						if i == len(lines[0]) - 1: #Is leaving
							gdir = 'LEAVE'
						
						elif lines[i+1][gpos[1]] == '#': #turns left
							gdir = 'left'
							gpos = (i, gpos[1])
							break
				case _: #Leaves
					fin = True

		return False


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

	threads = []
	val = {"val":0}
	lock = threading.Lock()
	for i in range(0, len(lines), 10):
		new_thread = SearchingThread(arlines, i, i+10, gpos, lock, val)
		threads.append(new_thread)
		new_thread.start()
		
	
	for t in threads:
		t.join()

	print(f"Possible obstacles: {val['val']}")



if __name__ == '__main__':
	main()

