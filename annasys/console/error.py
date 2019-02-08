from .log import log

def error(message):
    log('ERROR', message, fg='red', bold=True, color_status=True, arrow = ' ! ', include_brackets=True)
