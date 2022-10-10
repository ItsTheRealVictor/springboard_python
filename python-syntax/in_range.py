def in_range(nums, lowest, highest):
	"""Print numbers inside range.

	- nums: list of numbers
	- lowest: lowest number to print
	- highest: highest number to print

	For example:

	in_range([10, 20, 30, 40], 15, 30)

	should print:

	20 fits
	30 fits
	"""
	lower = [x for x in nums if x >= lowest]
	result = [y for y in lower if y <= highest]
	for res in result:
		print(f'{res} fits')
      
in_range([10, 20, 30, 40], 15, 30)