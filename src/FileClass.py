from importlib_metadata import files
import os
import shutil
class File:
    def __init__(self,extension:list,origin_dir:str,destination_dir:str):
        self.extension = list(extension)
        self.extension = list(map(lambda x: x.replace('.','') , self.extension))
        self.origin_dir = str(origin_dir)
        self.destination_dir = str(destination_dir)

    def create_directory(self,dir):
        try:
            os.mkdir(dir)
        except FileExistsError:
            self.delete_directory(dir)
            os.mkdir(dir)

    def delete_directory(self,dir):
        shutil.rmtree(dir)

    def list_files(self,path:str):
        files_extension = list(filter(lambda x: (x.split('.')[-1] in self.extension) , os.listdir(path)))
        return files_extension

    def movies_files(self):
        files = self.list_files(self.origin_dir)
        print(f'files:{files}')
        for filename in files:
            print(f'moving file {filename}')
            try:
                shutil.move(self.origin_dir+filename,self.destination_dir)
                print('successfully moved to self.destination_dir ') 
            except FileNotFoundError:
                print(f'fail in moved. Create directory {self.destination_dir}')
                self.create_directory(self.destination_dir)
    
