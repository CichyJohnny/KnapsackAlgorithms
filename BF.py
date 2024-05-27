class BruteForce:
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
        best_binary = []
        max_value = 0

        for i in range(2 ** self.n):
            binary = list(map(int, list(bin(i)[2:].zfill(self.n))))
            weight = 0
            value = 0

            for j in range(self.n):
                if binary[j]:
                    weight += self.items[j][0]
                    value += self.items[j][1]

            if weight <= self.c and value > max_value:
                max_value = value
                best_binary = binary

        used_items = [num + 1 for num, i in enumerate(best_binary) if i]

        return max_value, used_items


if __name__ == "__main__":
    bf = BruteForce()
    bf.read_from_file()
    value, items = bf.solve()

    print("Max value:", value)
    print("Used items:", *items)
