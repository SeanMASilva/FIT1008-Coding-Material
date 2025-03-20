from unittest import TestCase

from data_structures.linked_list import LinkedList
from data_structures.array_list import ArrayList


class TestArrayList(TestCase):
    def setUp(self):
        self.list = ArrayList()
    
    def test_append(self):
        self.list.append(1)
        self.assertEqual(len(self.list), 1)
        self.list.append(2)
        self.assertEqual(len(self.list), 2)
        
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 2)

    def test_insert(self):
        self.list.insert(0, 1)
        self.assertEqual(len(self.list), 1)
        self.list.insert(1, 2)
        self.assertEqual(len(self.list), 2)
        self.list.insert(1, 3)
        self.assertEqual(len(self.list), 3)
        
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 3)
        self.assertEqual(self.list[2], 2)
    
    def test_remove(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(len(self.list), 3)
        
        self.list.remove(1)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[0], 2)
        self.assertEqual(self.list[1], 3)
        
        self.list.remove(3)
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list[0], 2)

        self.list.remove(2)
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())
    
    def test_clear(self):
        for i in range(10):
            self.list.append(i)
        self.assertEqual(len(self.list), 10)

        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())
    
    def test_index(self):
        for i in range(10):
            self.list.append(i + 1)
        
        self.assertEqual(self.list.index(1), 0)
        self.assertEqual(self.list.index(5), 4)
        self.assertEqual(self.list.index(10), 9)

        # Add a second 1
        self.list.append(1)
        # Should still return the first 1
        self.assertEqual(self.list.index(1), 0)
    
    def test_len(self):
        for i in range(10):
            self.list.append(i)
            self.assertEqual(len(self.list), i + 1)
        
        for i in range(10):
            self.list.remove(i)
            self.assertEqual(len(self.list), 9 - i)


class TestLinkedList(TestCase):
    def setUp(self):
        self.list = LinkedList()
    
    def test_append(self):
        self.list.append(1)
        self.assertEqual(len(self.list), 1)
        self.list.append(2)
        self.assertEqual(len(self.list), 2)
        
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 2)

    def test_insert(self):
        self.list.insert(0, 1)
        self.assertEqual(len(self.list), 1)
        self.list.insert(1, 2)
        self.assertEqual(len(self.list), 2)
        self.list.insert(1, 3)
        self.assertEqual(len(self.list), 3)
        
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 3)
        self.assertEqual(self.list[2], 2)
    
    def test_remove(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(len(self.list), 3)
        
        self.list.remove(1)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[0], 2)
        self.assertEqual(self.list[1], 3)
        
        self.list.remove(3)
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list[0], 2)

        self.list.remove(2)
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())
    
    def test_clear(self):
        for i in range(10):
            self.list.append(i)
        self.assertEqual(len(self.list), 10)

        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())
    
    def test_index(self):
        for i in range(10):
            self.list.append(i + 1)
        
        self.assertEqual(self.list.index(1), 0)
        self.assertEqual(self.list.index(5), 4)
        self.assertEqual(self.list.index(10), 9)

        # Add a second 1
        self.list.append(1)
        # Should still return the first 1
        self.assertEqual(self.list.index(1), 0)
    
    def test_len(self):
        for i in range(10):
            self.list.append(i)
            self.assertEqual(len(self.list), i + 1)
        
        for i in range(10):
            self.list.remove(i)
            self.assertEqual(len(self.list), 9 - i)
