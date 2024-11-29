import os
import sys

sys.path.append("./project")

from something_module import X


class Y(X):
    i: int


if __name__ == "__main__":
    y = Y(1)
    print(y.x())
