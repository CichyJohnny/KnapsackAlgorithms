class GreedyAlgorithm:
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
        sort_items = sorted(self.items, key=lambda x: x[1], reverse=True)
        max_value = 0
        used_items = []

        for i in range(self.n):
            if self.c >= sort_items[i][0]:
                self.c -= sort_items[i][0]
                max_value += sort_items[i][1]
                used_items.append(self.items.index(sort_items[i]) + 1)

            if self.c == 0:
                break

        return max_value, used_items


if __name__ == "__main__":
    ga = GreedyAlgorithm()
    ga.read_from_file()
    value, items = ga.solve()

    print("Max value:", value)
    print("Used items:", *sorted(items))
