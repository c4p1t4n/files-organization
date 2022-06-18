import unittest
import src.organization as organization
import os
import sys
import shutil
from pathlib import Path

class testClass(unittest.TestCase):
    def test_moves(self):
        """
        Pegando variavel de ambiente home
        deleta caso exista pasta temporaria
        e criando pasta temporaria test
        """
        PATH = os.getenv('HOME')
        shutil.rmtree(PATH+'/test/')
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
        
        
