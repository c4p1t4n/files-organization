import os
import shutil

pastes = {
   'images': os.getenv('HOME')+'/Downloads/Images/',
   'drawio': os.getenv('HOME')+'/Downloads/Drawio/',
   'documents': os.getenv('HOME')+'/Documents/documents/',
   'compress': os.getenv('HOME')+'/Downloads/compression/'
}
def listFiles(path):
    dir = os.getenv('HOME')+'/Downloads' ;
    return os.listdir(dir)

    
def categories_files(listFiles):
    current_dir = os.getenv('HOME')+'/Downloads/'
    for filename in listFiles:
        try:
            if(filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg')):
                movies_files(current_dir+filename,pastes['images']+filename)
        except FileNotFoundError:
            os.mkdir(pastes['images'])
            movies_files(current_dir+filename,pastes['images']+filename)
        try:
            if(filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf')):
                movies_files(current_dir+filename,pastes['documents']+filename)
        except FileNotFoundError:
            os.mkdir(pastes['documents'])
            movies_files(current_dir+filename,pastes['documents']+filename)
        try:
            if(filename.endswith('.drawio')):
                movies_files(current_dir+filename,pastes['drawio']+filename)
        except FileNotFoundError:
            os.mkdir(pastes['drawio'])
            movies_files(current_dir+filename,pastes['drawio']+filename)
        try:
            if(filename.endswith('.zip') or filename.endswith('.deb') or filename.endswith('.tar.bz2') or filename.endswith('.gz') or filename.endswith('.tar.xz')):
                movies_files(current_dir+filename,pastes['compress']+filename)
        except FileNotFoundError:
            os.mkdir(pastes['compress'])
            movies_files(current_dir+filename,pastes['compress']+filename)
        

        
def movies_files(current_dir, destination_dir):
    shutil.move(current_dir, destination_dir)
    
def main():
    dir = listFiles('/Downloads')
    categories_files(dir)

if __name__ == '__main__':
    main()