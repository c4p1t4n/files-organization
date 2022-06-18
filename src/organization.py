import os
import shutil


"""
TODO: pegar pastes do input do terminal args -k key -p folder/destionation/file
"""
pastes = {
   'images': os.getenv('HOME')+'/Downloads/images/',
   'drawio': os.getenv('HOME')+'/Downloads/drawio/',
   'documents': os.getenv('HOME')+'/Documents/documents/',
   'compression': os.getenv('HOME')+'/Downloads/compression/'
}

def listFiles(path):
    dir = os.getenv('HOME')+ path ;
    return os.listdir(dir)

    
def categories_files(listFiles):
    current_dir = os.getenv('HOME')+'/Downloads/'
    for filename in listFiles:
        if(filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg')):
            movies_files(current_dir+filename,pastes['images']+filename)
        elif(filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf')):
            movies_files(current_dir+filename,pastes['documents']+filename)
        elif(filename.endswith('.drawio')):
            movies_files(current_dir+filename,pastes['drawio']+filename)  
        elif(filename.endswith('.zip') or filename.endswith('.deb') or filename.endswith('.tar.bz2') or filename.endswith('.gz') or filename.endswith('.tar.xz')):
            movies_files(current_dir+filename,pastes['compress']+filename)
        

        
def movies_files(current_dir, destination_dir):
    try:
        shutil.move(current_dir, destination_dir) 
    except FileNotFoundError:
        destination_dir.split('/')[-2]

def main():
    dir = listFiles('/test')
    print(dir)

if __name__ == '__main__':
    main()