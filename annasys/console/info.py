from .log import log

def info(message):
    log('INFO', message, fg='cyan', bold=True, color_status=True, include_brackets=True)
