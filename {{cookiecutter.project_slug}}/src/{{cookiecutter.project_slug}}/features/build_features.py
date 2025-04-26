# -*- coding: utf-8 -*-
import logging

def main():
    """ Runs feature engineering scripts."""
    logger = logging.getLogger(__name__)
    logger.info('building features')
    # TODO: Add feature engineering logic here
    pass

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
