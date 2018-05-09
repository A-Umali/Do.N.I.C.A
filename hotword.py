from precise_runner import PreciseEngine, PreciseRunner
from argparse import ArgumentParser
from subprocess import Popen
from threading import Event

def main():
    parser = ArgumentParser('Implementation demo of precise-engine')
    parser.add_argument('engine', help='Location of binary engine file')
    parser.add_argument('model')
    engine = PreciseEngine('precise-engine', 'active.wav')
    PreciseRunner(engine, on_activation=lambda:print('hello'))
    Event().wait()  # Wait forever


if __name__ == '__main__':
    main()
