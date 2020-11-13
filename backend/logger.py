import logging

LOGGER = logging.getLogger("connect4")
LOGGER.setLevel(logging.ERROR)
stream = logging.StreamHandler()
handler = logging.Formatter('%(name)s %(levelname)s: %(message)s')
stream.setFormatter(handler)
LOGGER.addHandler(stream)