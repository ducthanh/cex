import sys
from subprocess import call
import click
import unicodedata

HEADLESS = 'hl'


@click.option('-h', default=False, help='run your test with Headless if -h = True')
@click.option('-e', default='staging', help='your test environment')
@click.option('-c', default='sg', help='your test country')
@click.option('-t', default='123456,12,1212,1212', help='run with your tag or list of tags')

@click.command()


def cex(h,e,c,t):
    cm = 'bundle exec' + ' cucumber' + ' -p ' + profile_builder(e, c, h) + ' -t ' + tags_builder(t)
    call(cm, shell=True)

def tags_builder(t):
	t = t.split(',')
	for i in xrange(len(t)):
		t[i] = '@' + t[i]
	t = ','.join(t)
	unicodedata.normalize('NFKD', t).encode('ascii','ignore')
	return t

def profile_builder(e, c, hl = False):
	if hl is True:
		p = '.'.join([HEADLESS,e,c])
	else:
		p = '.'.join([e,c])
	return 'hp.' + p

if __name__=='__main__':
    cex()
