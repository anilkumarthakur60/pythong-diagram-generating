from graphviz import Digraph

# Create a new directed graph
dfd = Digraph(format='png', comment="Level 1 DFD for E-commerce System")

# Define entities, processes, and data stores
# External Entities
dfd.node('Customer', 'Customer', shape='rectangle')
dfd.node('Admin', 'Admin', shape='rectangle')

# Processes
dfd.node('P1', 'View Products', shape='circle')
dfd.node('P2', 'Register/Login', shape='circle')
dfd.node('P3', 'Add to Cart', shape='circle')
dfd.node('P4', 'Checkout', shape='circle')
dfd.node('P5', 'Update Order Status', shape='circle')

# Data Stores
dfd.node('DS1', 'Product Catalog', shape='cylinder')
dfd.node('DS2', 'User Accounts', shape='cylinder')
dfd.node('DS3', 'Cart Items', shape='cylinder')
dfd.node('DS4', 'Order Database', shape='cylinder')

# Add connections
# Guest interactions
dfd.edge('Customer', 'P1', 'Browse Products')
dfd.edge('P1', 'DS1', 'Retrieve Products')

# User registration/login
dfd.edge('Customer', 'P2', 'Register/Login')
dfd.edge('P2', 'DS2', 'Save User Data')

# Adding to cart
dfd.edge('Customer', 'P3', 'Select Products')
dfd.edge('P3', 'DS1', 'Retrieve Product Info')
dfd.edge('P3', 'DS3', 'Save Cart Items')

# Checkout
dfd.edge('Customer', 'P4', 'Place Order')
dfd.edge('P4', 'DS3', 'Retrieve Cart Items')
dfd.edge('P4', 'DS4', 'Save Order Details')

# Admin interactions
dfd.edge('Admin', 'P5', 'Update Order Status')
dfd.edge('P5', 'DS4', 'Modify Order Data')

# Render the graph
dfd.render('/Users/anilthakur/Desktop/python/images/ecommerce_level1_dfd', view=True)
