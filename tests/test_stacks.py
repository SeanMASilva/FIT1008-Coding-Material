from unittest import TestCase

from data_structures.linked_stack import LinkedStack


class TestLinkedStack(TestCase):
    
    def setUp(self):
        self.stack = LinkedStack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
    
    def test_len(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 2)
        self.stack.pop()
        self.assertEqual(len(self.stack), 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        # Push 1 to 10 to the stack
        for i in range(10):
            self.stack.push(i + 1)
        self.assertEqual(self.stack.peek(), 10)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_clear(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(self.stack), 0)
        self.assertRaises(Exception, self.stack.pop)
        self.assertRaises(Exception, self.stack.peek)
