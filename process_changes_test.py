import unittest

from process_changes import *

class TestProcessChanges(unittest.TestCase):

    def setUp(self):
        self.commit = Commit()

    def test_get_commit_comment(self):
        self.assertTrue( self.commit.get_commit_comment >= 0 )
        self.assertFalse ( self.commit.get_commit_comment  < 0 )
        
    def test_most_common(self):
        self.assertTrue( most_common >= 0 )
        self.assertFalse ( most_common < 0 )
    

if __name__ == '__main__':
    unittest.main()
