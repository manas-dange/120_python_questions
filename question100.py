class Logger:
    def log(self, message):
        print(f"Log: {message}")

class Calculator:
    def add(self, a, b):
        return a + b

class LoggingCalculator(Logger, Calculator):
    def log_and_add(self, a, b):
        result = self.add(a, b)
        self.log(f"The result of adding {a} and {b} is {result}")
        return result

# Example
lc = LoggingCalculator()
lc.log_and_add(5, 3)
