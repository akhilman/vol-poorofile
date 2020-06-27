from jinja2 import FileSystemLoader, Environment

TEMPLATE_FILE = 'profile.pine'

template_loader = FileSystemLoader(searchpath='./')
template_env = Environment(loader=template_loader)

template = template_env.get_template(TEMPLATE_FILE)
output = template.render()
print(output)
