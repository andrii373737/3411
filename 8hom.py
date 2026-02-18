import logging

logging.basicConfig(
    level=logging.ERROR,
    filename='logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    print(10 / 0)
except Exception as e:
    logging.error(f"Error occurred: {e}")