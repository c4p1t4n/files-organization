import unittest
import src.organization as organization
import os
import sys
import shutil
from pathlib import Path

class testClass(unittest.TestCase):
    def test_list_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pasta temporaria test
        """
        PATH = os.getenv('HOME')
        testCurrentDirectory = PATH+'/test'
        if os.path.isdir(testCurrentDirectory):
            shutil.rmtree(testCurrentDirectory)
        os.mkdir(testCurrentDirectory)
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
    def test_move_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pastas temporarias para teste
        """
        PATH = os.getenv('HOME')
        testCurrentDirectory = PATH+'/test'
        testMoveDirectory = PATH+'/testMovieFiles'
        if os.path.isdir(testCurrentDirectory) and os.path.isfile(testMoveDirectory) :
            shutil.rmtree(testCurrentDirectory)
            shutil.rmtree(testMoveDirectory)
        elif os.path.isdir(testCurrentDirectory):
            shutil.rmtree(testCurrentDirectory)
        elif os.path.isfile(testMoveDirectory):
            shutil.rmtree(testMoveDirectory)    
        os.mkdir(testCurrentDirectory)
        os.mkdir(testMoveDirectory)
        """
        Criando arquivo temporario de 
        """
        file = open(PATH+'/test/file.txt' , 'w+')
        file.close
        self.assertEqual(len(organization.listFiles(PATH+'/testMovieFiles')),0)
        """
        Movendo arquivo
        """
        organization.movies_files(PATH+'/test',PATH+'/testMovieFiles')
        self.assertEqual(len(organization.listFiles(PATH+'/testMovieFiles')),1)
        

        
        
