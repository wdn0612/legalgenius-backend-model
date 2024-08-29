import logging
from dotenv import load_dotenv
import os

# set up a global logger
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# set up global environment variables
if os.environ.get('ENV') == 'test':
    load_dotenv('.env.test')
elif os.environ.get('ENV') == 'uat':
    load_dotenv('.env.uat')
elif os.environ.get('ENV') == 'prod':
    load_dotenv('.env.prod')
else:
    logger.error('Environment not set.')
    exit()
