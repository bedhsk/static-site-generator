import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_different_tag(self):
        children = [HTMLNode("p", "hola mundo")]
        node = HTMLNode(
            "a",
            children=children,
            props={"href": "https://google.com", "target": "_blank"},
        )
        node2 = HTMLNode(
            "div",
            children=children,
            props={"href": "https://google.com", "target": "_blank"},
        )
        self.assertNotEqual(node, node2)

    def test_eq_different_value(self):
        node = HTMLNode("p", "hello world")
        node2 = HTMLNode("p", "hola mundo")
        self.assertNotEqual(node, node2)

    def test_eq_different_children(self):
        children1 = [HTMLNode("p", "hello world")]
        children2 = [HTMLNode("p", "hola mundo")]
        node = HTMLNode("div", children=children1)
        node2 = HTMLNode("div", children=children2)
        self.assertNotEqual(node, node2)

    def test_eq_different_props(self):
        node = HTMLNode("a", props={"href": "https://google.com"})
        node2 = HTMLNode("a", props={"href": "https://example.com"})
        self.assertNotEqual(node, node2)

    def test_eq_null_values(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_mixed_attributes(self):
        node = HTMLNode("div", "content", None, {"class": "container"})
        node2 = HTMLNode("div", "content", None, {"class": "container"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = HTMLNode(
            "div",
            "Hello World",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )

    def test_values(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "what a strange world", None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, what a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()
