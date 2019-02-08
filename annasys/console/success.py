from .log import log

def success(message):
    log('SUCCESS', message, fg='green', bold=True, color_status=True, include_brackets=True)
