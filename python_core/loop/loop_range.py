"""
    + range() = range(stop): If stop <= 0, we get an empty sequence

    + range(two_params) = range(start, stop): If start >= stop, we get an empty sequence

        range(2, 5)   =  [2, 3, 4]
        range(-2, 4)  =  [-2, -1, 0, 1, 2, 3]
        range(4, 2)   =  []

    + range(start, stop, step)

        range(2, 10, 3)   =  [2, 5, 8]
        range(4, -1, -1)  =  [4, 3, 2, 1, 0]

    + The default value of 'start' = 0, and the default value of 'step' = 1
"""

if __name__ == '__main__':
    print(list(range(4, 4)))
