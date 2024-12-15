from graphviz import Digraph

# Create ER Diagram
er_diagram = Digraph('ER_Diagram', format='png')
er_diagram.attr(rankdir='LR', size='20')  # Increase size for higher resolution

# Entities
entities = {
    'users': ['id', 'email', 'password', 'type'],
    'categories': ['id', 'name'],
    'products': ['id', 'name', 'category_id', 'description', 'price', 'image', 'status'],
    'orders': ['id', 'user_id', 'total_amount', 'shipping_address', 'phone', 'status', 'payment_method', 'notes'],
    'order_items': ['id', 'order_id', 'product_id', 'quantity', 'unit_price', 'total_price']
}

for entity, attributes in entities.items():
    er_diagram.node(entity, shape='record', label='{{{}|{}}}'.format(entity, '|'.join(attributes)))

# Relationships
relationships = [
    ('products', 'categories', 'category_id', 'id', 'SET NULL'),
    ('orders', 'users', 'user_id', 'id', 'SET NULL'),
    ('order_items', 'orders', 'order_id', 'id', 'CASCADE'),
    ('order_items', 'products', 'product_id', 'id', 'SET NULL')
]

for src, dst, src_attr, dst_attr, on_delete in relationships:
    er_diagram.edge(src, dst, label='{} -> {} (ON DELETE {})'.format(src_attr, dst_attr, on_delete))

# Render ER Diagram
er_diagram.render('/Users/anilthakur/Desktop/python/ER_Diagram', cleanup=True)

# Path to image
er_diagram_path = "/Users/anilthakur/Desktop/python/ER_Diagram.png"

er_diagram_path
