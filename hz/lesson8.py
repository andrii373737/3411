import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename = 'Readme.log',
    filemode = 'w',
    format = 'We have next logging message: %(asctime)s, %(levelname)s, %(message)s'
)

logging.debug('debug i td')
logging.info('info i td')
logging.warning('warning i td')
logging.error('error i td')
logging.critical('critical i td')







