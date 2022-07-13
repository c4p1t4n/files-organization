from pathlib import Path
import unittest
import src.organization as organization
import os
import sys
import shutil
from src.FileClass import File


class testClass(unittest.TestCase):
    def delete_directory(self,dir):
        shutil.rmtree(dir)
        
    def create_directory(self,dir):
        try:
            os.mkdir(dir)
        except FileExistsError:
            self.delete_directory(dir)
            os.mkdir(dir)

    def get_directory(self,name_directory):
        """
        Criando variaveis para os diretorios
        """
        HOME = os.getenv('HOME')
        PATH = HOME + name_directory
        """
        Criando os diretorios
        """
        try:
            os.mkdir(PATH)
        except:
            self.delete_directory(PATH)
            os.mkdir(PATH)

        return PATH

    def test_list_files(self):
        """
        Criando diretorios temporarios
        """
        test_current_directory = self.get_directory('/test_current_directory/')
        test_destination_directory = self.get_directory('/test_destination_directory/')
        """
        Instanciando Objeto
        """
        text = File(['.txt'],test_current_directory,test_destination_directory,)
        """
        Criando arquivo temporarios
        """
        file_txt = open(test_current_directory+'file.txt' , 'w+')
        file_txt.close
        file_img = open(test_current_directory+'file.img' , 'w+')
        file_img.close
        ################
        self.assertEqual(len(text.list_files(test_current_directory)),1)
        """
        Deletando diretorios temporarios
        """
        self.delete_directory(test_current_directory)
        self.delete_directory(test_destination_directory)
    


    def test_move_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pastas temporarias para teste
        """
        test_destination_directory = self.get_directory('/test_destination_directory/')
        test_current_directory = self.get_directory('/teste_current_directory/')
        
        # if os.path.isfile(testMoveDirectory) and os.path.isdir(test_current_directory):
        #     self.delete_directory(test_current_directory)
        #     self.delete_directory(testMoveDirectory)
        # elif os.path.isdir(test_current_directory):
        #     self.delete_directory(test_current_directory)
        # elif os.path.isfile(testMoveDirectory):
        #     self.delete_directory(testMoveDirectory)
                
        # self.create_directory(test_current_directory)
        # self.create_directory(testMoveDirectory)
        """
        Instanciando Objeto
        """
        text = File(['.txt','txt'],test_current_directory,test_destination_directory)
        """
        Criando arquivo temporario de 
        """
        file = open(test_current_directory+'file.txt' , 'w+')
        file.close
        self.assertEqual(len(text.list_files(test_destination_directory)),0)
        self.assertGreaterEqual(len(text.list_files(test_current_directory)),1)
        """
        Movendo arquivo
        """
        text.movies_files()
        self.assertEqual(len(text.list_files(test_destination_directory)),1)

    
        



if __name__ == '__main__':
    unittest.main()
    