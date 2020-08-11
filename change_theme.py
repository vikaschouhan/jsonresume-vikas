#!/usr/bin/env python3
import argparse
import os
import sys

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('--tdir', help='Theme directory', type=str, default=None)
    args    = parser.parse_args()

    if args.__dict__['tdir'] == None:
        print('--tdir required.')
        sys.exit(-1)
    # endif

    ifile = 'index.js'
    tdir  = os.path.expanduser(args.__dict__['tdir'])
    rfile = os.path.join(tdir, ifile)
    assert os.path.isdir(tdir), '>> ERROR:: Directory "{}" doesnot exist !!'.format(tdir)
    assert os.path.isfile(rfile), '>> ERROR:: File "{}" doesnot exist !!'.format(rfile)

    if os.path.isfile(ifile):
        os.remove(ifile)
    # endif
    os.symlink(rfile, ifile)
# endif
