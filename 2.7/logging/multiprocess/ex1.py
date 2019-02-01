import logging
import multiprocessing
import time

import mplog

FORMAT = '%(asctime)s - %(processName)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
existing_logger = logging.getLogger('x')


def subprocess(n):
    existing_logger.info('y')
    logger = logging.getLogger('sub')
    logger.info('Before sleep.')
    time.sleep(0.01)
    logger.info('After sleep.')

    root = logging.getLogger()
    root.debug('Root log message.')


def start_processes(log_queue):
    procs = list()
    for i in xrange(5):
        proc = multiprocessing.Process(target=mplog.logged_call,
                                       args=(log_queue, subprocess, i))
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()


def main():
    existing_logger.info('Before')
    with mplog.open_queue() as log_queue:
        existing_logger.info('In context manager.')
        start_processes(log_queue)
        existing_logger.info('At the end.')

    logging.info('Now really quitting.')


if __name__ == '__main__':
    main()
