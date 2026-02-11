import logging

logging.basicConfig(
    level=logging.INFO,
    filename = 'Запуск програми пройшов успішно.log',
    filemode = 'w',
    format = 'We have next logging message: %(asctime)s, %(levelname)s, %(message)s'
)

logging.info('ПРОГРАМА УСПІШНО ЗАПУСТИЛАСЬ')

