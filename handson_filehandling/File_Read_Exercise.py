#primary file reading exercise
import os

def read_chunk(fname, startpos, endpos):
    #not validating the positions
    try:
        f_handle = open(fname)
        #move the file pointer to startpos
        f_handle.seek(startpos, 0)
        qty =endpos - startpos

        #reading byte by byte
        #for i in range(qty):
        #    print(f_handle.read(1), end = '')

        #reading in one buffer
        print(f_handle.read(qty))

        f_handle.close()

    except:
        print('File Read Error')

def get_file_size(fname):
    if os.path.exists(fname):
        return os.stat(fname).st_size
    return -1 #file doesnt exist

def file_read(fname):
    try:
        #open a file in read mode (file must exist, otherwise FileNotFoundError is raised)
        f_handle = open(fname, 'r')

        #iterate over the file line by line
        #for x in f_handle:
        #    print(x, end='')

        #read the entire file
        #big_buffer = f_handle.read()
        #print(big_buffer)

        #read files in chunks of 20 bytes each
        chunk_size = 20
        while True:
            chunk = f_handle.read(chunk_size) #fetch bytes equal to chunk_size, returns a buffer of chunk_size and increments the file pointer by chunk_size. For the last chunk the available bytes are read and returned.
            if not chunk: #chunk is False at EOF
                break
            print(chunk, end='')

        #close the file (free the resource)
        f_handle.close()
    except:
        print('File Read Error')



def main():
    #print(get_file_size('d:/temp/a.txt'))
    #file_read('d:/temp/a.txt')
    read_chunk('d:/temp/a.txt', 2, 11)

main()


