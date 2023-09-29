import os
import logging
import datetime

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)


# Configure the logger
def debug(msg, *args, **kwargs):
    logging.basicConfig(
        filename=os.path.join(log_folder, f"debug_{datetime.datetime.now().date()}.log"),
        level=logging.DEBUG,
        datefmt='%Y-%m-%d:%H:%M:%S',
        format=f"%(levelname)-6s: %(message)s (%(asctime)s)"
    )
    return logging.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    logging.basicConfig(
        filename=os.path.join(log_folder, f"access_{datetime.datetime.now().date()}.log"),
        level=logging.INFO,
        format=f"%(levelname)-6s: %(message)s (%(asctime)s)"
    )
    formatter = logging.Formatter(f"%(levelname)-6s: %(message)s (%(asctime)s)")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    logging.basicConfig(
        filename=os.path.join(log_folder, f"warning_{datetime.datetime.now().date()}.log"),
        level=logging.WARNING,
        format=f"%(levelname)-6s: %(message)s (%(asctime)s)"
    )
    return logging.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logging.basicConfig(
        filename=os.path.join(log_folder, f"error_{datetime.datetime.now().date()}.log"),
        level=logging.ERROR,
        format=f"%(levelname)-6s: %(message)s (%(asctime)s)"
    )
    return logging.error(msg, *args, **kwargs)
