from graphviz import Digraph

# Create a new directed graph
dfd = Digraph(format='png', comment="Level 1 DFD for COD-Only E-commerce System")

# Define entities, processes, and data stores
# External Entities
dfd.node('Customer', 'Customer', shape='rectangle')
dfd.node('Admin', 'Admin', shape='rectangle')

# Processes
dfd.node('P1', 'Place Order', shape='circle')
dfd.node('P2', 'Manage Inventory', shape='circle')
dfd.node('P3', 'Handle Delivery', shape='circle')
dfd.node('P4', 'Generate Reports', shape='circle')

# Data Stores
dfd.node('DS1', 'Product Catalog', shape='cylinder')
dfd.node('DS2', 'Order Database', shape='cylinder')

# Add connections
# Customer interactions
dfd.edge('Customer', 'P1', 'Browse Products')
dfd.edge('P1', 'DS1', 'Retrieve Products')
dfd.edge('P1', 'DS2', 'Save Order Details')
dfd.edge('P1', 'P3', 'Place COD Order')

# Delivery process
dfd.edge('P3', 'Customer', 'Deliver Order')
dfd.edge('P3', 'DS2', 'Update Order Status')

# Admin interactions
dfd.edge('Admin', 'P2', 'Update Inventory')
dfd.edge('P2', 'DS1', 'Modify Products')
dfd.edge('Admin', 'P4', 'Request Reports')
dfd.edge('P4', 'DS2', 'Fetch Order Data')
dfd.edge('P4', 'Admin', 'Send Reports')

# Render the graph
dfd.render('/Users/anilthakur/Desktop/python/images/ecommerce_cod_dfd', view=True)
