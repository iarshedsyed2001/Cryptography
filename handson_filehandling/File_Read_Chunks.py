import os

class FileManager:
    def __init__(self, fname):
        if not os.path.exists(fname):
            raise FileExistsError(fname + ' doesn\'t exist')
        self.fname = fname
        self.number_of_chunks = 4
        self.chunk_positions = self.__divide_into_chunks__()
        print(self.chunk_positions)
        for x,y in self.chunk_positions:
            self.read_chunk(x,y)

    def __divide_into_chunks__(self):
        size = os.stat(self.fname).st_size #say 1002
        start = 0
        end = -1
        qty = size // self.number_of_chunks # say 250
        positions = []
        for i in range(self.number_of_chunks-1):
            start = end + 1 #0,250,500,750
            end = start + qty -1 #249,499,749,999
            positions.append((start,end))
        #for the remaining odd
        positions.append((end+1, size)) #1000-1002
        return positions


    def read_chunk(self,  startpos, endpos):
        #not validating the positions
        try:
            f_handle = open(self.fname)
            #move the file pointer to startpos
            f_handle.seek(startpos, 0)
            qty =endpos - startpos

            #reading in one buffer
            print(f_handle.read(qty))

            print('--------------')

            f_handle.close()

        except:
            print('File Read Error')


def main():
    fm = FileManager('d:/temp/a.txt')

main()