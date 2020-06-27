from jinja2 import FileSystemLoader, Environment

TEMPLATE_FILE = 'profile.pine'
params = {
    'n_rows': 10,
    'n_bars': 25,
    'n_blocks': 20,
    'avg_lenght': 20,
    'row_multiplier': 0.6,
    'block_colors': ['aqua', 'orange'],
    'recent_n_bars': 50,
    'recent_block_color': 'gray'
}

template_loader = FileSystemLoader(searchpath='./')
template_env = Environment(loader=template_loader)

template = template_env.get_template(TEMPLATE_FILE)

output = template.render(**params)
print(output)
