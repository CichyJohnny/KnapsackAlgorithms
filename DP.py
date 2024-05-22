class DynamicProgramming:
    def __init__(self):
        self.n = 0
        self.c = 0
        self.items = []

    def read_from_input(self):
        self.n = int(input("Enter the number of items: "))
        self.c = int(input("Enter the knapsack capacity: "))

        for i in range(self.n):
            w, v = map(int, input(f"{i+1}: ").split())
            self.items.append((w, v))

    def read_from_file(self):
        with open("items.txt", 'r') as file:
            self.n, self.c = map(int, file.readline().split())

            for i in range(self.n):
                w, v = map(int, file.readline().split())
                self.items.append((w, v))

    def solve(self):
        matrix = [[0 for _ in range(self.c+1)] for _ in range(self.n+1)]

        for i in range(1, self.n+1):
            w, v = self.items[i - 1]
            for j in range(1, self.c+1):
                if j < w:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w] + v)

        max_value = matrix[self.n][self.c]
        used_items = []

        for i in range(self.n, 0, -1):
            if matrix[i][self.c] != matrix[i-1][self.c]:
                used_items.append(i)
                self.c -= self.items[i-1][0]

        return max_value, used_items[::-1]


if __name__ == "__main__":
    dp = DynamicProgramming()
    dp.read_from_file()
    value, items = dp.solve()

    print("Max value:", value)
    print("Used items:", *items)
