# -*- coding: utf-8 -*-
import logging

def main():
    """ Trains the model."""
    logger = logging.getLogger(__name__)
    logger.info('training model')
    # TODO: Add model training logic here
    pass

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
