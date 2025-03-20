from unittest import TestCase

from data_structures.linked_queue import LinkedQueue


class TestLinkedQueue(TestCase):
    def setUp(self):
        self.queue = LinkedQueue()
    
    def test_append(self):
        self.queue.append(1)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.append(2)
        self.assertEqual(self.queue.peek(), 1)
    
    def test_len(self):
        self.queue.append(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.append(2)
        self.assertEqual(len(self.queue), 2)
        self.queue.serve()
        self.assertEqual(len(self.queue), 1)
        self.queue.peek()
        self.assertEqual(len(self.queue), 1)

    def test_serve(self):
        self.queue.append(1)
        self.queue.append(2)
        self.queue.append(3)
        self.assertEqual(self.queue.serve(), 1)
        self.assertEqual(self.queue.peek(), 2)
        self.assertEqual(self.queue.serve(), 2)
        self.assertEqual(self.queue.peek(), 3)
        self.assertEqual(self.queue.serve(), 3)
        self.assertTrue(self.queue.is_empty())
    
    def test_peek(self):
        for i in range(10):
            self.queue.append(i + 1)
        self.assertEqual(self.queue.peek(), 1)
        for i in range(10):
            self.queue.serve()
            if i < 9:
                self.assertEqual(self.queue.peek(), i + 2)
        self.assertTrue(self.queue.is_empty())

    def test_peek_node(self):
        self.queue.append(1)
        self.assertEqual(self.queue.peek_node().item, 1)
        self.queue.append(2)
        self.assertEqual(self.queue.peek_node().item, 1)
        self.queue.serve()
        self.assertEqual(self.queue.peek_node().item, 2)
        self.assertEqual(self.queue.peek_node().link, None)
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.append(1)
        self.assertFalse(self.queue.is_empty())
    
    def test_clear(self):
        self.queue.append(1)
        self.queue.append(2)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)
        self.assertRaises(Exception, self.queue.serve)
        self.assertRaises(Exception, self.queue.peek)
