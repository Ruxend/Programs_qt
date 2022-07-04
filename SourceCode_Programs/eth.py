class eth():
	def ethkey(eth):
		keys = []
		if not eth:
			# If eth is a string it's empty, just return blank list
			return keys
		# Start with the first character already in last
		last, eth = eth[0], eth[1:]
		# If last is int we start at offset 1
		if last.isdigit():
			keys.append('')
		for i in eth:
			if i.isdigit() is last.isdigit():
				# Keep accumulating same type chars
				last += i
			else:
				# Save and restart next round
				keys.append(int(last) if last.isdigit() else last)
				last = i
		# Save final round and return
		keys.append(int(last) if last.isdigit() else last)
		return keys

