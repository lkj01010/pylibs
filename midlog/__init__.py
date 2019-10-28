import colorlog
from colorlog import ColoredFormatter

handler = colorlog.StreamHandler()

formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s (%(module)s:%(lineno)d) %(levelname)-8s%(reset)s %(message_log_color)s%(message)s ",
    datefmt="%y/%m/%d %H:%M:%S",
    reset=True,
    log_colors={
        'DEBUG': 'white',
        'INFO': 'white',
        'WARNING': 'white',
        'ERROR': 'white',
        'CRITICAL': 'black,bg_white',
    },
    secondary_log_colors={
        'message': {
            'DEBUG': 'blue',
            'INFO': 'cyan',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red'
        }
    },
    style='%'
)
handler.setFormatter(formatter)

log = colorlog.getLogger('example')
log.addHandler(handler)
log.setLevel('DEBUG')