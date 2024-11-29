from typing import Any


from ..functions.x import x


class X:
    """x class"""

    i: Any

    def __init__(self, i: Any):
        self.i = i

    def x(self) -> Any:
        """_summary_

        :return: _description_
        :rtype: Any
        """
        return x(self.i)
