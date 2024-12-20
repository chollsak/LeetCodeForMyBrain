arr = [1111,7644,1107,6978,8742,1,7403,7694,9193,4401,377,8641,5311,624,3554,6631]
counterIndex = []
result = []

for i in range(len(arr)):
    binary_repr = bin(arr[i])[2:]
    
    counter = binary_repr.count('1')
    counterIndex.append(counter)

bits = [{"n": n, "nbits": bits, "binary_len": len(bin(n)[2:])} for n, bits in zip(arr, counterIndex)]

sorted_arr = sorted(
    bits, key=lambda bit:(bit["nbits"], bit["n"])
)

for n in sorted_arr:
    result.append(n["n"])

print(result)