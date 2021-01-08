from .pantilt import pantilthat_cls

__version__ = '0.0.1'

main_class = pantilthat_cls()
servo_enable = main_class.servo_enable
pan = main_class.pan
tilt = main_class.tilt
