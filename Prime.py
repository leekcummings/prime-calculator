class Prime:
    def __init__(self, p: int, c: int):
        self._prime = p

        # comp is the next composite number with this prime factor
        self._comp = c

    def add_comp(self):
        """Changes the coord to the following factor of the prime that is not divisible by 2.
        Multiplying the prime by 2 prevents even coords"""
        self._comp += 2*self._prime

    def __str__(self):
        return (f"{self._prime}: {self._comp}\n")