import unittest

import triton


class ImportTest(unittest.TestCase):

  def test_basic(self):
    print(dir(triton))
    self.assertTrue(triton.jit)
    self.assertTrue(triton.compiler)


if __name__ == '__main__':
  unittest.main()
