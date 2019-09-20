import BitVector
import itertools
# bv = BitVector.BitVector(bitlist = [0]*8)
# bv_1 = bv[:]
# print(bv)
# bv[6] = 1
# print(bv, bv_1)
f = open("plaintext.txt", "r")
txt = f.read()
# list1 = []
# for i in range(len(txt)//8):
#     list1.append(txt[i*8])
#
# print(list1)
# # print("T")
# for i in list1:
#     if i == 'T':
#         print(1)
# print(txt)
# final_list = []
# numbytes = 8
# for j in range(8):
#     temp_list = []
#     for i in range(len(txt)//numbytes):
#         temp_char = txt[i*numbytes + j]
#         temp_list.append(temp_char)
#     print(temp_list.count(' '))
#     print(temp_list.count('e'))
#     final_list.append(max(set(temp_list), key = temp_list.count))
# print(final_list)
# print(BitVector.BitVector(textstring = ' '))
# print(ord(' '))
# print(ord('\x16')^ord(' '))
# print(ord('6'))
# list_n = [' ', 'e']
# list_char = []
# for a in list_n:
#     for b in list_n:
#         for c in list_n:
#             for d in list_n:
#                 for e in list_n:
#                     for f in list_n:
#                         for g in list_n:
#                             for h in list_n:
#                                 list_char.append([a, b, c, d, e, f, g, h])
# print(list_char)
# print(len(list_char), 2**8)

print(txt.count("the"))

# comb = itertools.combination(list_n, 2)
# perm = itertools.perm
# for i in list(comb):
#     print(i)
