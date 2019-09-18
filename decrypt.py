import BitVector

PassPhrase = "I want to learn cryptograph and network security"

BLOCKSIZE = 64
numbytes = BLOCKSIZE // 8



bv_iv = BitVector.BitVector(bitlist = [0]*BLOCKSIZE)
for i in range(0,len(PassPhrase) // numbytes):
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes]
    bv_iv ^= BitVector.BitVector( textstring = textstr )

key = "bits@f463"

key_bv = BitVector.BitVector(bitlist = [0]*BLOCKSIZE)
for i in range(0,len(key) // numbytes):
    keyblock = key[i*numbytes:(i+1)*numbytes]
    key_bv ^= BitVector.BitVector( textstring = keyblock )

f = open("encrypt.txt", "r")
hex = f.read()
# print(len(hex))
bv = BitVector.BitVector(hexstring = hex)
# print(len(bv))
f.close()

msg_bv = BitVector.BitVector( size = 0 )

previous_block = bv_iv
# bv = BitVector( filename = "plaintext.txt" )
for i in range(len(bv)//BLOCKSIZE):
    # bv_read = bv.read_bits_from_file(BLOCKSIZE)
    # if len(bv_read) < BLOCKSIZE:
        # bv_read += BitVector(size = (BLOCKSIZE - len(bv_read)))

    bv_read = bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
    temp_read = bv_read.deep_copy()
    bv_read ^= key_bv
    bv_read ^= previous_block
    previous_block = temp_read
    msg_bv += bv_read

f_1 = open("plaintext.txt", 'r')
bin = f_1.read()
bv_1 = BitVector.BitVector(textstring = bin)
msg_bv = msg_bv.get_bitvector_in_ascii()
print(msg_bv)
