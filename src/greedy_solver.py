from knapsack import KnapsackSolver

class KnapsackGreedySolver(KnapsackSolver):
    def __init__(self, instance):
        super().__init__(instance)
        self._inst = instance
        self.weight = None
        self.value = None
    
    def solve(self):

        ratios = [(i, self._inst.V[i] / self._inst.W[i]) for i in range(self._inst.size)]
        sorted_items = sorted(ratios, key=lambda x: x[1], reverse=True)
        items = [i for i, _ in sorted_items]


        total_weight = 0
        total_value = 0
        self._X = [0] * self._inst.size

        for i in items:
            if total_weight + self._inst.W[i] <= self._inst.C:
                self._X[i] = 1
                total_weight += self._inst.W[i]
                total_value += self._inst.V[i]

        self.weight = total_weight
        self.value = total_value

        return tuple(self._X)