import click

def log(status, message=None, fg='white', bold=False, color_status=False, width=12, arrow=None, include_brackets=False):
    if not status and message is None:
        click.echo('')
        return

    arrow = ' -> ' if arrow is None else arrow

    if message is None:
        message = status
        status = ''

    if status:
        status_width = width - 2 if include_brackets else width
        status = '{:>{width}}'.format(status, width=status_width)

    message = str(message)
    status = str(status)

    if color_status:
        status = click.style(status, fg=fg, bold=bold)
    else:
        message = click.style(message, fg=fg, bold=bold)

    if status:
        if include_brackets:
            status = f'[{status}]'
        click.echo(f'{status}{arrow}{message}')
    else:
        click.echo(f'{"":{width}}{arrow}{message}')
