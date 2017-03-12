import sys
from subprocess import call
import click

@click.option('-h', default=False, help='run your test with Headless if -h = True')
@click.option('-t', default=123456, help='run with your tag or list of tags')
@click.option('-p', default='hp.staging.ph', help='run with your profile')


@click.command()

def cex(t, p):
    cmd= 'bundle exec' + ' cucumber' + ' -t ' + t + ' -p ' + p
    print(cmd)
    call(cmd, shell=True)

def tags_builder
	'1234'
def profile_builder(hl = False)
	'hp.'

if __name__=='__main__':
    cex()
