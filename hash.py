import glob
import hashlib
import sys
import os
import zlib

#CHUNKSIZE = int(input('Chunk size: ')) # a chunk size
LBA_SIZE = 512
total_chunks_num = 0 
unique_chunks_num = 0 

def show_dedupe_rate(total_chunks_num, unique_chunks_num): #calculate dedupe_rate
    print ('Num of chunks                  = ', total_chunks_num)
    print ('Num of duplicate chunks        = ', total_chunks_num - unique_chunks_num)
    print ('Dedupe rate can be achieved to = ', (1.0 - (float(unique_chunks_num)/total_chunks_num))*100, '%')

def page_FP_4k_dedup():
    CHUNKSIZE = 4096
    global total_chunks_num
    global unique_chunks_num
    output_file_page_FP = open('/mnt/c/Users/Ron/Desktop/fp_4k.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file
                afile.seek(CHUNKSIZE, 1) #move to next chunk

def page_FP_8k_dedup():
    CHUNKSIZE = 8192
    global total_chunks_num
    global unique_chunks_num
    output_file_page_FP = open('/mnt/c/Users/Ron/Desktop/fp_8k.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file
                afile.seek(CHUNKSIZE, 1) #move to next chunk

def page_FP_16k_dedup():
    CHUNKSIZE = 16384
    global total_chunks_num
    global unique_chunks_num
    output_file_page_FP = open('/mnt/c/Users/Ron/Desktop/fp_16k.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file
                afile.seek(CHUNKSIZE, 1) #move to next chunk

def page_FP_32k_dedup():
    CHUNKSIZE = 32768
    global total_chunks_num
    global unique_chunks_num
    output_file_page_FP = open('/mnt/c/Users/Ron/Desktop/fp_32k.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file

def sector_FP_dedup():
    global total_chunks_num
    global unique_chunks_num
    output_file_sector_FP = open('/mnt/c/Users/Ron/Desktop/fp_512B.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Test FP:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_sector_FP.writelines(fingerprint + '\n') #write fp into output file

def sector_CRC_generator():
    global total_chunks_num
    global unique_chunks_num
    output_file_sector_CRC = open('/mnt/c/Users/Ron/Desktop/crc_512B.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/input_linux/*"): #input path
        print('Generate CRC:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                crc = zlib.crc32(cur_chunk)
                check_duplicate = crc in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[crc] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                total_chunks_num += 1
                output_file_sector_CRC.writelines(str(hex(crc)[2:]) + '\n') #write fp into output file

page_FP_4k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)

total_chunks_num = 0
unique_chunks_num = 0
page_FP_8k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)

total_chunks_num = 0
unique_chunks_num = 0
page_FP_16k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)

total_chunks_num = 0
unique_chunks_num = 0
page_FP_32k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)

total_chunks_num = 0
unique_chunks_num = 0
sector_FP_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)

total_chunks_num = 0
unique_chunks_num = 0
sector_CRC_generator()
show_dedupe_rate(total_chunks_num, unique_chunks_num)