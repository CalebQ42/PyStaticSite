import unittest

from blocks import markdown_to_blocks


class Tests(unittest.TestCase):
    def txt_to_blocks(self):
        txt = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertEqual(
            markdown_to_blocks(txt),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )

if __name__ == "__main__":
    unittest.main()