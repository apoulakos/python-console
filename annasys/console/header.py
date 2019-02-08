"""console.header displays a simple header"""
import click

def header(message, width=80, fg='green', bold=True):
    message = click.style(' {} '.format(message.upper()), fg=fg, bold=bold)
    click.echo('\n{:-^{width}}'.format(message, width=width))
