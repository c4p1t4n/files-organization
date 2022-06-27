from pathlib import Path
import unittest
import src.organization as organization
import os
import sys
import shutil


class testClass(unittest.TestCase):
    def delete_directory(self,dir):
        shutil.rmtree(dir)
    def create_directory(self,dir):
        try:
            os.mkdir(dir)
        except FileExistsError:
            self.delete_directory(dir)
            os.mkdir(dir)
    def test_list_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pasta temporaria test
        """
        PATH = os.getenv('HOME')
        testCurrentDirectory = PATH+'/test'
        if os.path.isdir(testCurrentDirectory):
           self.delete_directory(testCurrentDirectory)
        self.create_directory(testCurrentDirectory)
        """
        Criando arquivo temporario
        """
        file = open(testCurrentDirectory+'/file.txt' , 'w+')
        file.close
        
        """
        Listando arquivos
        """
        list = organization.listFiles('/test')
        self.assertEqual(len(list),1)
        file = open(testCurrentDirectory+'/file2.txt' , 'w+')
        file.close
        list = organization.listFiles('/test')
        self.assertEqual(len(list),2)
        """
        Deletando arquivos e pastas
        """
        shutil.rmtree(testCurrentDirectory)
    """
    TODO: resolver o problema de arquivo já existente e de arquivo não existente
    
    """
    def test_move_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pastas temporarias para teste
        """
        PATH = os.getenv('HOME')
        testCurrentDirectory = PATH+'/test'
        testMoveDirectory = PATH+'/testMovieFiles'
        if os.path.isfile(testMoveDirectory) and os.path.isdir(testCurrentDirectory):
            self.delete_directory(testCurrentDirectory)
            self.delete_directory(testMoveDirectory)
        elif os.path.isdir(testCurrentDirectory):
            self.delete_directory(testCurrentDirectory)
        elif os.path.isfile(testMoveDirectory):
            self.delete_directory(testMoveDirectory)
                
        self.create_directory(testCurrentDirectory)
        self.create_directory(testMoveDirectory)
        """
        Criando arquivo temporario de 
        """
        file = open(testCurrentDirectory+'/file2.txt' , 'w+')
        file.close
        self.assertEqual(len(organization.listFiles(PATH+'/testMovieFiles')),0)
        """
        Movendo arquivo
        """
        organization.movies_files(PATH+'/test',PATH+'/testMovieFiles')
        self.assertEqual(len(organization.listFiles(PATH+'/testMovieFiles')),1)
        

        
        
