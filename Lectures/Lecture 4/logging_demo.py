import logging


logger = logging.getLogger()
logging.basicConfig(filename="logging_demo.log", level=logging.DEBUG)

def my_function():
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

if __name__ == '__main__':
    my_function()