import BitVector

PassPhrase = "I want to learn cryptograph and network security"

BLOCKSIZE = 64
numbytes = BLOCKSIZE // 8



bv_iv = BitVector.BitVector(bitlist = [0]*BLOCKSIZE)
for i in range(0,len(PassPhrase) // numbytes):
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes]
    bv_iv ^= BitVector.BitVector( textstring = textstr )


# f = open("encrypt.txt", "r")
f = open("ciphertext.txt", "r")
hex = f.read()
# print(len(hex))
bv = BitVector.BitVector(hexstring = hex)
# print(len(bv))
f.close()

encrypt_bv = BitVector.BitVector( size = 0 )

previous_block = bv_iv
# bv = BitVector( filename = "plaintext.txt" )
for i in range(len(bv)//BLOCKSIZE):
    bv_read = bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
    temp_read = bv_read.deep_copy()
    bv_read ^= previous_block
    previous_block = temp_read
    encrypt_bv += bv_read

encrypt_ascii = encrypt_bv.get_bitvector_in_ascii()
# print(encrypt_ascii)
final_list = []
# final_list1 = []
for j in range(8):
    temp_list = []
    for i in range(len(encrypt_ascii)//numbytes):
        temp_char = encrypt_ascii[i*numbytes + j]
        temp_list.append(temp_char)
    # print(temp_list)
    # num = 0
    # for i in range(1, len(temp_list)):
    #     if temp_list.count(temp_list[i]) > temp_list.count(temp_list[num]):
    #         num = i
    # final_list1.append(temp_list[num])
    final_list.append(max(set(temp_list), key = temp_list.count))
print(final_list)

list_n = [' ', 'e']
list_char = []
for a in list_n:
    for b in list_n:
        for c in list_n:
            for d in list_n:
                for e in list_n:
                    for f in list_n:
                        for g in list_n:
                            for h in list_n:
                                list_char.append([a, b, c, d, e, f, g, h])
# for li in [[' ']*8, ['e']*8, ['t']*8]:
decrypt_list = []
for li in list_char:
    key_temp = BitVector.BitVector(size = 0)
    for i in range(numbytes):
        tmp_key = BitVector.BitVector(textstring = final_list[i])
        tmp_key ^= BitVector.BitVector(textstring = li[i])
        # print(tmp_key.get_bitvector_in_ascii())
        key_temp += tmp_key

    decrpyt_file = BitVector.BitVector(size = 0)
    for i in range(len(encrypt_bv)//BLOCKSIZE):
        tmp_block = encrypt_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
        tmp_block ^= key_temp
        # print(tmp_block.get_bitvector_in_ascii())
        decrpyt_file += tmp_block

    decrypt_text = decrpyt_file.get_bitvector_in_ascii()
    # print(key_temp.get_bitvector_in_ascii())
    # print(decrypt_text)
    decrypt_list.append([decrypt_text, key_temp.get_bitvector_in_ascii()])

max_i = 0
max_i_a = decrypt_list[0][0].count("and")
max_i_t = decrypt_list[0][0].count("the")
for i in range(1, len(decrypt_list)):
    temp_a = decrypt_list[i][0].count("and")
    temp_t = decrypt_list[i][0].count("the")
    if temp_a > max_i_a and temp_t > max_i_t:
        max_i_a = temp_a
        max_i_t = temp_t
        max_i = i
print(decrypt_list[max_i][0], decrypt_list[max_i][1])
# print(len(decrypt_list))

fr = open("recoveredtext.txt", 'w')
fr.write(decrypt_list[max_i][0])
