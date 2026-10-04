from .moduleA import x
from . import moduleA

__all__ = ['x', 'moduleA']
print('pkgA imported')