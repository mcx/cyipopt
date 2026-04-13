from warnings import warn

msg = (f"The module {__name__} is deprecated as of version 1.7.0. Use 'from "
       "cyipopt import ipopt_wrapper' instead of 'import ipopt_wrapper'.")
warn(msg, DeprecationWarning, stacklevel=2)

# NOTE : I assume that no one has code in the wild that does something like:
# import ipopt_wrapper
# ipopt_wrapper.__doc__
# and only imports the most likely used variables which include what __all__
# provided in ipopt_wrapper and more.
from cyipopt.ipopt_wrapper import (
    CREATE_PROBLEM_MSG,
    CyIpoptEvaluationError,
    DTYPEd,
    DTYPEi,
    INF,
    IPOPT_VERSION,
    Problem,
    STATUS_MESSAGES,
    set_logging_level,
)
