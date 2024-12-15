from graphviz import Digraph

# Create Level 0 DFD
level_0 = Digraph('Level_0_DFD', format='png')
level_0.attr(rankdir='LR', size='10')

# External entities
level_0.node('User', shape='box', style='filled', color='lightblue', label='User')
level_0.node('Admin', shape='box', style='filled', color='lightcoral', label='Admin')

# Processes
level_0.node('Ecommerce System', shape='circle', style='filled', color='lightgreen', label='Ecommerce\nSystem')

# Data stores
data_stores = ['Users', 'Orders', 'Products', 'Categories']
for store in data_stores:
    level_0.node(store, shape='cylinder', style='filled', color='lightyellow', label=store)

# Connections
level_0.edge('User', 'Ecommerce System', label='View Products')
level_0.edge('User', 'Ecommerce System', label='Place Order')
level_0.edge('User', 'Ecommerce System', label='Checkout')
level_0.edge('User', 'Ecommerce System', label='View Order Status')
level_0.edge('Admin', 'Ecommerce System', label='Manage Products')
level_0.edge('Admin', 'Ecommerce System', label='Manage Categories')
level_0.edge('Admin', 'Ecommerce System', label='Manage Order Status')
level_0.edge('Ecommerce System', 'Users', label='Store/Retrieve User Data')
level_0.edge('Ecommerce System', 'Orders', label='Store/Retrieve Orders')
level_0.edge('Ecommerce System', 'Products', label='Store/Retrieve Products')
level_0.edge('Ecommerce System', 'Categories', label='Store/Retrieve Categories')

# Render Level 0
level_0.render('/Users/anilthakur/Desktop/python/images/Level_0_DFD', cleanup=True)

# Create Level 1 DFD
level_1 = Digraph('Level_1_DFD', format='png')
level_1.attr(rankdir='LR', size='10')

# Processes
processes = {
    'User Management': 'Manage Users',
    'Order Management': 'Manage Orders',
    'Product Management': 'Manage Products',
    'Category Management': 'Manage Categories'
}
for process, label in processes.items():
    level_1.node(process, shape='circle', style='filled', color='lightgreen', label=label)

# Data stores
for store in data_stores:
    level_1.node(store, shape='cylinder', style='filled', color='lightyellow', label=store)

# External entities
level_1.node('User', shape='box', style='filled', color='lightblue', label='User')
level_1.node('Admin', shape='box', style='filled', color='lightcoral', label='Admin')

# Connections Level 1
level_1.edge('User', 'User Management', label='User Data')
level_1.edge('User Management', 'Users', label='Store/Retrieve')
level_1.edge('User', 'Order Management', label='Order Data')
level_1.edge('Order Management', 'Orders', label='Store/Retrieve')
level_1.edge('Admin', 'Product Management', label='Product Data')
level_1.edge('Product Management', 'Products', label='Store/Retrieve')
level_1.edge('Admin', 'Category Management', label='Category Data')
level_1.edge('Category Management', 'Categories', label='Store/Retrieve')

# Render Level 1
level_1.render('/Users/anilthakur/Desktop/python/images/Level_1_DFD', cleanup=True)

# Create Level 2 DFD
level_2 = Digraph('Level_2_DFD', format='png')
level_2.attr(rankdir='LR', size='10')

# Sub-processes
sub_processes = {
    'Register User': 'Register',
    'Authenticate User': 'Authenticate',
    'Place Order': 'Place Order',
    'Checkout': 'Checkout',
    'View Order Status': 'View Status',
    'Add Product': 'Add',
    'Update Product': 'Update',
    'Categorize Product': 'Categorize',
    'Update Order Status': 'Update'
}
for sp, label in sub_processes.items():
    level_2.node(sp, shape='ellipse', style='filled', color='lightpink', label=label)

# External entities
level_2.node('User', shape='box', style='filled', color='lightblue', label='User')
level_2.node('Admin', shape='box', style='filled', color='lightcoral', label='Admin')

# Data stores
for store in data_stores:
    level_2.node(store, shape='cylinder', style='filled', color='lightyellow', label=store)

# Connections Level 2
level_2.edge('User', 'Register User', label='Registration Data')
level_2.edge('Register User', 'Users', label='Store')
level_2.edge('User', 'Authenticate User', label='Login Data')
level_2.edge('Authenticate User', 'Users', label='Validate')
level_2.edge('User', 'Place Order', label='Order Data')
level_2.edge('Place Order', 'Orders', label='Store')
level_2.edge('User', 'Checkout', label='Payment Data')
level_2.edge('Checkout', 'Orders', label='Update')
level_2.edge('User', 'View Order Status', label='Request Status')
level_2.edge('View Order Status', 'Orders', label='Retrieve')
level_2.edge('Admin', 'Add Product', label='Product Data')
level_2.edge('Add Product', 'Products', label='Store')
level_2.edge('Admin', 'Update Product', label='Product Data')
level_2.edge('Update Product', 'Products', label='Update')
level_2.edge('Admin', 'Categorize Product', label='Category Data')
level_2.edge('Categorize Product', 'Categories', label='Update')
level_2.edge('Admin', 'Update Order Status', label='Order Status Data')
level_2.edge('Update Order Status', 'Orders', label='Update')

# Render Level 2
level_2.render('/Users/anilthakur/Desktop/python/images/Level_2_DFD', cleanup=True)

# Create Use Case Diagram
use_case = Digraph('Use_Case_Diagram', format='png')
use_case.attr(rankdir='TB', size='10')

# Actors
use_case.node('User', shape='box', style='filled', color='lightblue', label='User')
use_case.node('Admin', shape='box', style='filled', color='lightcoral', label='Admin')

# Use Cases
use_cases = [
    'View Products', 'Place Order', 'Checkout', 'View Order Status',
    'Manage Products', 'Manage Categories', 'Manage Order Status'
]
for uc in use_cases:
    use_case.node(uc, shape='ellipse', style='filled', color='lightgrey', label=uc)

# Connections
use_case.edge('User', 'View Products')
use_case.edge('User', 'Place Order')
use_case.edge('User', 'Checkout')
use_case.edge('User', 'View Order Status')
use_case.edge('Admin', 'Manage Products')
use_case.edge('Admin', 'Manage Categories')
use_case.edge('Admin', 'Manage Order Status')

# Render Use Case Diagram
use_case.render('/Users/anilthakur/Desktop/python/images/Use_Case_Diagram', cleanup=True)

# Create System Flow Chart
flow_chart = Digraph('System_Flow_Chart', format='png')
flow_chart.attr(rankdir='TB', size='30,20')

# Start/End
flow_chart.node('Start', shape='ellipse', style='filled', color='lightgreen', label='Start')
flow_chart.node('End', shape='ellipse', style='filled', color='lightgreen', label='End')

# Processes
flow_chart.node('Login', shape='box', style='filled', color='lightblue', label='Login')
flow_chart.node('Browse', shape='box', style='filled', color='lightblue', label='Browse Products')
flow_chart.node('Add to Cart', shape='box', style='filled', color='lightblue', label='Add to Cart')
flow_chart.node('Checkout', shape='box', style='filled', color='lightblue', label='Checkout')
flow_chart.node('Payment', shape='box', style='filled', color='lightblue', label='Payment')
flow_chart.node('Confirmation', shape='box', style='filled', color='lightblue', label='Order Confirmation')

# Decision
flow_chart.node('Valid Login?', shape='diamond', style='filled', color='lightyellow', label='Valid Login?')
flow_chart.node('Stock Available?', shape='diamond', style='filled', color='lightyellow', label='Stock Available?')
flow_chart.node('Payment Successful?', shape='diamond', style='filled', color='lightyellow', label='Payment Successful?')

# Connections
flow_chart.edge('Start', 'Login')
flow_chart.edge('Login', 'Valid Login?')
flow_chart.edge('Valid Login?', 'Browse', label='Yes')
flow_chart.edge('Valid Login?', 'Login', label='No')
flow_chart.edge('Browse', 'Add to Cart')
flow_chart.edge('Add to Cart', 'Stock Available?')
flow_chart.edge('Stock Available?', 'Checkout', label='Yes')
flow_chart.edge('Stock Available?', 'Browse', label='No')
flow_chart.edge('Checkout', 'Payment')
flow_chart.edge('Payment', 'Payment Successful?')
flow_chart.edge('Payment Successful?', 'Confirmation', label='Yes')
flow_chart.edge('Payment Successful?', 'Checkout', label='No')
flow_chart.edge('Confirmation', 'End')

# Render System Flow Chart
flow_chart.render('/Users/anilthakur/Desktop/python/images/System_Flow_Chart', cleanup=True)

# Create Gantt Chart
gantt_chart = Digraph('Gantt_Chart', format='png')
gantt_chart.attr(rankdir='TB', size='10')

# Tasks
tasks = [
    ('Task 1', '2023-01-01', '2023-01-10'),
    ('Task 2', '2023-01-11', '2023-01-20'),
    ('Task 3', '2023-01-21', '2023-02-10'),
    ('Task 4', '2023-02-11', '2023-02-20'),
    ('Task 5', '2023-02-21', '2023-03-01'),
    ('Task 6', '2023-03-02', '2023-03-10'),
    ('Task 7', '2023-03-11', '2023-03-20'),
    ('Task 8', '2023-03-21', '2023-03-31')
]

for task, start, end in tasks:
    gantt_chart.node(task, shape='box', style='filled', color='lightblue', label=f'{task}\n{start} to {end}')

# Connections
for i in range(len(tasks) - 1):
    gantt_chart.edge(tasks[i][0], tasks[i + 1][0])

# Render Gantt Chart
gantt_chart.render('/Users/anilthakur/Desktop/python/images/Gantt_Chart', cleanup=True)

# # Paths to images
# level_0_path = "/Users/anilthakur/Desktop/python/images/Level_0_DFD.png"
# level_1_path = "/Users/anilthakur/Desktop/python/images/Level_1_DFD.png"
# level_2_path = "/Users/anilthakur/Desktop/python/images/Level_2_DFD.png"
# use_case_path = "/Users/anilthakur/Desktop/python/images/Use_Case_Diagram.png"
# flow_chart_path = "/Users/anilthakur/Desktop/python/images/System_Flow_Chart.png"
# gantt_chart_path = "/Users/anilthakur/Desktop/python/images/Gantt_Chart.png"

# level_0_path, level_1_path, level_2_path, use_case_path, flow_chart_path, gantt_chart_path

# source venv/bin/activate  # On macOS/Linux
# python main.py  # Run the script
