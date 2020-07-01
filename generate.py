from jinja2 import BaseLoader, Environment
import click
import re


class KeyValueParamType(click.ParamType):
    name = 'key=val'

    def convert(self, value, param, ctx):
        found = re.findall(r'^(\w+?)=(.+?)$', value)
        if not found:
            self.fail(f'expected "key=value", got {value!r}')
        return tuple(found[0])


KEY_VAL = KeyValueParamType()


def split_filter(value, delimiter=','):
    return str(value).split(delimiter)


@click.command()
@click.argument('template', type=click.File('r'))
@click.argument('output', default='-', type=click.File('w'))
@click.option('-o', '--option', type=KEY_VAL, multiple=True)
def main(template, output, option):
    env = Environment(loader=BaseLoader)
    env.filters['split'] = split_filter
    templ = env.from_string(template.read())
    code = templ.render(**dict(option))
    output.write(code)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
