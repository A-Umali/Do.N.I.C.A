import re
import speedtest
import logging
import asyncio

TITLE = ['CLOSE-PROGRAM']


def handle(title, message):
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test())
        print('Finished')
    except Exception as e:
        raise e
    finally:
        loop.close()


def is_valid(title):
    return bool(re.search('command.close.program', title, re.I))


async def test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    print(s.upload() + ' and ' + s.download())

