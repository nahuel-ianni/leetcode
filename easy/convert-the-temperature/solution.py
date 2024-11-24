# Solution for the 'Convert the Temperature' problem.
# Time complexity: O(1).
# Space complexity: O(1).

class Solution:
    def convertTemperature(self, celsius: float) -> Tuple[float, float]:
        kelvin = celsius + 273.15
        farenheit = celsius * 1.80 + 32

        return kelvin, farenheit
    
    # The original exercise used a List[float] as the return type.
    # By using a Tuple instead, the result is immutable, making it faster to 
    # create and slightly more efficient in terms of performance.
    # 
    # Example implementation using List:
    # def convertTemperature(self, celsius: float) -> List[float]:
    #     kelvin = celsius + 273.15
    #     fahrenheit = celsius * 1.80 + 32
    #
    #     return [kelvin, fahrenheit]
