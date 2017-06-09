def split_str_into_len(s, l=2):
	"""Split a string into chunks of length l"""
	return [s[i:i+l] for i in range(0, len(s), l)]

print split_str_into_len("abcdefghij")
