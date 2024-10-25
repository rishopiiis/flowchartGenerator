import networkx as nx
import matplotlib.pyplot as plt

# Define nodes with their positions
nodes = [
    ('HOD', {'label': 'HOD', 'pos': (0.1, 0.25)}),
]

# No edges, as it's a single node graph
edges = []

def create_and_save_graph(file_path):
    G = nx.DiGraph()

    # Add node
    for node_id, attributes in nodes:
        G.add_node(node_id, **attributes)

    # No edges to add (since there are none)

    # Position nodes and get labels
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_node_attributes(G, 'label')

    # Create a new figure
    fig, ax = plt.subplots(figsize=(6, 3))

    # Draw the single node
    nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightblue', ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_family='sans-serif', ax=ax)

    # Remove axis
    plt.axis('off')

    # Set title
    plt.title("Normal Leave Form")

    # Save the plot to the specified file path
    plt.savefig(file_path)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Specify the file path where you want to save the flow chart
    file_path = r"C:\Users\LENOVO\Downloads\CO200 Project\flow gen\single_node_chart.png"
    create_and_save_graph(file_path)
