class Counter:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def utility_message():
        print("This is a utility message.")

# Example
Counter.increment_count()
Counter.increment_count()
print("Count:", Counter.count)
Counter.utility_message()
