from jinja2 import FileSystemLoader, Environment

TEMPLATE_FILE = 'profile.pine'
params = {
    'n_bars': 20,
    'n_blocks': 20,
    'n_rows': 10,
    'block_colors': ['aqua', 'orange'],
    'last_block_color': 'blue'
}

template_loader = FileSystemLoader(searchpath='./')
template_env = Environment(loader=template_loader)

template = template_env.get_template(TEMPLATE_FILE)

output = template.render(**params)
print(output)
