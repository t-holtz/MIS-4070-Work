import unittest

def get_discount(price):
    """ Give 5% discount to purchases under $100, 10% discount to
        purchases under $1000, and 15% discount for purchases $1000 and over.
    """
    # Handle edge cases
    if price < 0:
        return 0.0
    if price < 100:
        return price * 0.05
    if price < 1000:
        return price * 0.10
    return price * 0.15

class DiscountTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(get_discount(-1), 0.0)

    def test_10(self):
        self.assertEqual(get_discount(10), 0.50)

    def test_500(self):
        self.assertEqual(get_discount(500), 50.0)

    def test_2000(self):
        self.assertEqual(get_discount(2000), 300.0)

if __name__ == "__main__":
    unittest.main()