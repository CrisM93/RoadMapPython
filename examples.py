from collections import deque
def bfs(graph, start_node):
    visited = set()  # Usar un conjunto para una verificación de membresía eficiente
    queue = deque([start_node])  # Usar deque para operaciones de cola eficientes
    visited.add(start_node)  # Marcar el nodo inicial como visitado

    while queue:
        current_node = queue.popleft()  # Desencolar un nodo del frente de la cola
        print(current_node, end=" ")  # Procesar el nodo (imprimir en este caso)

        for neighbor in graph[current_node]:  # Iterar sobre todos los vecinos del nodo actual
            if neighbor not in visited:  # Si el vecino no ha sido visitado aún
                queue.append(neighbor)  # Encolar al vecino
                visited.add(neighbor)  # Marcar al vecino como visitado
                visited.add(neighbor)  # Mark the neighbor as visited

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'B')  # Output: A B C D E F