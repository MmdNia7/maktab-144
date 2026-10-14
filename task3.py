import logging

logging.basicConfig(
    level=logging.INFO,
    # format="%(levelname)s: %(message)s"
)


class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.start = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.n:
            # logging.info("Iteration finished")
            logging.error("Iteration finished")
            raise StopIteration
        number = self.start
        self.start += 2
        logging.info("Generated number")
        return number


numbers = EvenNumbers(10)

for number in numbers:
    print(number)
