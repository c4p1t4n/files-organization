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
        if os.path.isdir(PATH+'/test'):
            shutil.rmtree(PATH+'/test')
        os.mkdir(PATH+'/test')
        """
        Criando arquivo temporario
        """
        file = open(PATH+'/test/file.txt' , 'w+')
        file.close
        """
        Listando arquivos
        """
        list = organization.listFiles('/test')
        self.assertEqual(len(list),1)
        """
        Deletando arquivos e pastas
        """
    def test_move_files(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pastas temporarias para teste
        """
        PATH = os.getenv('HOME')
        if os.path.isdir(PATH+'/test') and os.path.isfile(PATH+'/testMovieFiles') :
            shutil.rmtree(PATH+'/test/')
            shutil.rmtree(PATH+'/testMovieFiles')
        elif os.path.isdir(PATH+'/test'):
            shutil.rmtree(PATH+'/test/')
        elif os.path.isfile(PATH+'/testMovieFiles'):
            shutil.rmtree(PATH+'/testMovieFiles')
        os.mkdir(PATH+'/test')
        os.mkdir(PATH+'/testMovieFiles')
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
        

        
        
