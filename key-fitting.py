key = 'hello '
# key = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz zyxwuvtsrqponmlkjihgfedcbazyxwuvtsrqponmlkjihgfedcbazyxwuvtsrqponmlkjihgfedcba'

def fit_key(key):
	if (len(key) < 6):
		raise ValueError('key must be more than 6 bytes')
	elif (len(key) < 64):
		key_array = []

		for k in key:
			key_array.append(int(format(ord(k), '08b'), 2))

		result = key_array

		print('key_array ->', len(key_array), ':', key_array)

		while (len(result) < 64):
			result.append(result[len(result) - 1] ^ result[len(result) - 6])
	else:
		key_array = []

		for k in key:
			key_array.append(int(format(ord(k), '08b'), 2))

		while ((len(key_array) % 64) != 0):
			key_array.append(0)

		key_bytes = [key_array[i:(i + 64)] for i in range(0, len(key_array), 64)]
		result = key_bytes[len(key_bytes) - 1]

		for i in range(len(key_bytes) - 1):
			for j in range(len(key_bytes[i])):
				result[j] = result[j] ^ key_bytes[i][j]

	return result

res = fit_key(key)
print('res ->', len(res), ':', res)