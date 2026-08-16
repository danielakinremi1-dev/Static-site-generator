import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode("p", "sampletext", ["child1", "child2"], {"class": "my-class"})
        node2 = HTMLNode("p", "sampletext", ["child1", "child2"], {"class": "my-class"})
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode("p", "sampletext", ["child1", "child2"], None)
        node2 = HTMLNode("p", "sampletext", ["child1", "child2"], None)
        self.assertEqual(node, node2)

    def test_not_eq3(self):
        node = HTMLNode("a", "This is a text node", None, {"href": "http://example.com"})
        node2 = HTMLNode("a", "This is a different text node", None, {"href": "http://example.com"})
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = HTMLNode("p", "sampletext", ["child1", "child2"], {"class": "my-class", "href": "http://example.com"})
        node2 = HTMLNode("p", "sampletext", ["child1", "child2"], {"class": "my-class", "href": "http://example.com"})
        nodeprops = node.props_to_html()
        node2props = node2.props_to_html()
        self.assertEqual(nodeprops, node2props) 

    def test_not_eq5(self):
        node = HTMLNode("a", "This is a text node", None, {"hre": "http://example.com"})
        node2 = HTMLNode("a", "This is a different text node", None, {"href": "http://example.com"})
        nodeprops = node.props_to_html()
        node2props = node2.props_to_html()
        self.assertNotEqual(nodeprops, node2props)




        

    def test_leaf_to_html_p6(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 

    def test_leaf_to_html_p7(self):
        node = LeafNode("p", "Hello, world!", {"class": "my"})
        self.assertNotEqual(node.to_html(), '<p class="myclass">Hello, world!</p>')

    def test_leaf_to_html_p8(self):
        node = LeafNode("p", "Hello, world!", {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), '<p class="my-class" id="my-id">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()