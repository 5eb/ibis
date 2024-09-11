from __future__ import annotations

import functools
import inspect
from collections.abc import Callable
from typing import Any, TypeVar, overload

from koerce import Builder, Call, Deferred, Var


class _Variable(Var):
    def __repr__(self):
        return self.name


# reserved variable name for the value being matched
_ = Deferred(_Variable("_"))
