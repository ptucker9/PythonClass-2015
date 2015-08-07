import unittest #You need this module
import ordinal #This is the script you want to test


class mytest(unittest.TestCase):

  def test_ord(self):
    self.assertEqual("11th", ordinal.ordinal_type(11))
    
  def test_ord1(self):
    self.assertEqual("Put in an integer.", ordinal.ordinal_type(23.4))
    
  def test_ord2(self):
    self.assertEqual("13th", ordinal.ordinal_type(13))
        
  def test_ord3(self):
    self.assertEqual("2nd", ordinal.ordinal_type(2))        
        
  def test_two(self):
    thing1=ordinal.ordinal_type(22)
    thing2=ordinal.ordinal_type(23)
    self.assertNotEqual(thing1, thing2)
 
if __name__ == '__main__': #Add this if you want to run the test with this script.
	unittest.main()
