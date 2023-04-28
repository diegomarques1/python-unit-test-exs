import unittest
 
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32


# With a static method, I would make it this way, but the exercise asks for an instance of TemperatureConverter
class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(30), 86)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(25.5), 77.9)
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(18), 64.4)
        
# Alternative version: calls the method from an instance
# class TestTemperatureConverter(unittest.TestCase):
#     def test_celsius_to_fahrenheit(self):
#         conv = TemperatureConverter()
#         self.assertAlmostEqual(conv.celsius_to_fahrenheit(30), 86)
#         self.assertAlmostEqual(conv.celsius_to_fahrenheit(25.5), 77.9)
#         self.assertAlmostEqual(conv.celsius_to_fahrenheit(18), 64.4)

if __name__ == '__main__':
    unittest.main()