class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data
        return data

    def draw(self):
        print(*(i for i in transfer if i in (range(min(Graph.LIMIT_Y), max(Graph.LIMIT_Y)+1))))


graph_1 = Graph()
transfer = graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

graph_1.draw()
