from importlib_metadata import files
import os
import shutil
class File:
    def __init__(self,extension:list,current_dir:str,destination_dir:str):
        
        self.extension = list(extension)
        self.current_dir = str(current_dir)
        self.destination_dir = str(destination_dir)

    def createDirectory(self,dir):
        try:
            os.mkdir(dir)
        except FileExistsError:
            self.delete_directory(dir)
            os.mkdir(dir)
    def delete_directory(self,dir):
        shutil.rmtree(dir)

    def listFiles(self,path:str):
        return os.listdir(path)
        
    def moviesFiles(self,current_dir, destination_dir):
        files = self.listFiles(current_dir)
        for fileName in files:
            print(f'moving file {fileName}')
            try:
                shutil.move(current_dir, destination_dir)
                print('successfully moved') 
            except FileNotFoundError:
                print(f'fail in moved create directory {destination_dir}')
                self.create_directory(destination_dir)
    
