import unittest
from issue import Issue

class IssueTest(unittest.TestCase):

    def test_get_all_issues(self):
        lista = Issue.get_all_issues(['lista', 'lista2'])
        self.assertIsInstance(lista, list)


if __name__ == "__main__":
    unittest.main()