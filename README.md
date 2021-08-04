## Target
This program derives deduplication rate of a file in python

## Steps in this program:
1. Reading a file
2. Chunking in fixed-size method (4KB in example) 
3. Building a hash table
4. Hashing each chunk and insert its fingerprint into this hash table
5. Derive dedup rate
