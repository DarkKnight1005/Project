class MathHelper:
    def __init__(self):
        pass

    def truncate(self, n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier