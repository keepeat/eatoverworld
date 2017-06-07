import sphinx

import sys

if __name__ == '__main__':
    # for debug usage `python build_docs.py -b html source build -v -E`

    sphinx.build_main(sys.argv)
