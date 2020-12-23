import unittest
from ..rtree import *

class TestRTreeCreation(unittest.TestCase):
    def test_treeSmallerThanFour(self):
        pass
        #Arrange
        rtree = RTree()
        rtree.create_random_points(3)
        #Act
        for i in range(len(rtree.root.children())):
            
        #Assert
        self.assertTrue()
    
    def test_treeSmallerThanEight(self):
        #Arrange
        rtree = RTree()
        rtree.create_random_points(3)
        #Act

        #Assert
        self.assertTrue

    def test_BigTree(self):
        #Arrange
        rtree = RTree()
        rtree.create_random_points(3)
        #Act

        #Assert
        self.assertTrue