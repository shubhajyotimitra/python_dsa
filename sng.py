import heapq
from collections import deque, defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(list)   # adjacency list {user: [friends]}
        self.weights = defaultdict(dict) # edge weights

    # Add friendship
    def add_friendship(self, user1, user2, weight=1):
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)
        self.weights[user1][user2] = weight
        self.weights[user2][user1] = weight

    # BFS Friend Recommendation
    def recommend_friends_bfs(self, user):
        visited = set([user])
        queue = deque([(user, 0)])
        recommendations = set()

        while queue:
            current, level = queue.popleft()
            if level == 2:  # friends-of-friends
                recommendations.add(current)
            if level < 2:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

        recommendations.discard(user)
        recommendations -= set(self.graph[user])
        return list(recommendations)

    # Dijkstra Recommendation
    def recommend_friends_dijkstra(self, user):
        distances = {u: float('inf') for u in self.graph}
        distances[user] = 0
        pq = [(0, user)]
        visited = set()

        while pq:
            dist, current = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.graph[current]:
                new_dist = dist + self.weights[current][neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        recommendations = {u: d for u, d in distances.items()
                           if u != user and u not in self.graph[user]}
        return sorted(recommendations.items(), key=lambda x: x[1])

    # Visualize Graph
    def visualize_network(self, highlight_user=None, recommendations=None):
        G = nx.Graph()

        # Add nodes & edges
        for user, friends in self.graph.items():
            for friend in friends:
                G.add_edge(user, friend, weight=self.weights[user][friend])

        pos = nx.spring_layout(G)  # layout style

        # Draw nodes
        node_colors = []
        for node in G.nodes():
            if node == highlight_user:
                node_colors.append("red")  # current user
            elif recommendations and node in recommendations:
                node_colors.append("green")  # recommended friends
            else:
                node_colors.append("skyblue")

        # Draw graph
        nx.draw(G, pos, with_labels=True, node_size=2000,
                node_color=node_colors, font_size=10, font_weight="bold")

        # Draw edge weights
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.show()


# ===============================
# 🚀 Demo
# ===============================
if __name__ == "__main__":
    sn = SocialNetwork()

    # Add friendships
    sn.add_friendship("Alice", "Bob", 2)
    sn.add_friendship("Alice", "Charlie", 5)
    sn.add_friendship("Bob", "David", 1)
    sn.add_friendship("Charlie", "Eve", 2)
    sn.add_friendship("David", "Frank", 3)
    sn.add_friendship("Eve", "Grace", 2)

    # Recommendations
    bfs_recs = sn.recommend_friends_bfs("Alice")
    dijkstra_recs = sn.recommend_friends_dijkstra("Alice")

    print("\n🔎 BFS Recommendations for Alice:", bfs_recs)
    print("✨ Dijkstra Recommendations for Alice:", dijkstra_recs)

    # Visualization (highlight Alice + recommendations)
    sn.visualize_network("Alice", [rec[0] for rec in dijkstra_recs])
