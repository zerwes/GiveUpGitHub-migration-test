#! /usr/bin/env python3
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent

__doc__ = """
simple test script only
"""

import sys

def main(args):
    """main function"""
    print('test: OK : %s' % ':'.join(args))
    sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
