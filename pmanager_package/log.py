import click


def log(message, color):
    click.secho(message, fg=color)


def info(message):
    log(message, 'green')
