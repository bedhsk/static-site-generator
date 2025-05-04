import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Testing url", TextType.TEXT, None)
        test = TextNode("Testing url", TextType.TEXT)
        self.assertEqual(node, test)

    def test_repr(self):
        node = TextNode("Testing repr", TextType.TEXT, "https://www.bot.dev")
        self.assertEqual("TextNode(Testing repr, text, https://www.bot.dev)", repr(node))


if __name__ == "__main__":
    unittest.main()
