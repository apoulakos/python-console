from .log import log

def warning(message):
    log('WARN', message, fg='yellow', bold=True, color_status=True, include_brackets=True)
