#!/usr/bin/env python3
import argparse
import os
import sys

def rm_file(f):
    if os.path.isfile(f) or os.path.islink(f):
        os.remove(f)
    # endif
# enddef

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('--tdir', help='Theme directory', type=str, default=None)
    parser.add_argument('--json', help='Resume json file', type=str, default=None)
    args    = parser.parse_args()

    if args.__dict__['tdir'] is None or args.__dict__['json'] is None:
        print('All arguments required !!')
        sys.exit(-1)
    # endif

    theme_dir    = os.path.expanduser(args.__dict__['tdir'])
    resume_json  = os.path.expanduser(args.__dict__['json'])

    # Set index.js
    dst = 'index.js'
    src = os.path.join(theme_dir, dst)
    assert os.path.isdir(theme_dir), '>> ERROR:: Directory "{}" doesnot exist !!'.format(theme_dir)
    assert os.path.isfile(src), '>> ERROR:: File "{}" doesnot exist !!'.format(src)
    rm_file(dst)
    print('>> {} -> {}'.format(src, dst))
    os.symlink(src, dst)

    # Set resume.json
    dst = 'resume.json'
    src = resume_json
    assert os.path.isfile(src), '>> ERROR:: File "{}" doesnot exist !!'.format(src)
    rm_file(dst)
    print('>> {} -> {}'.format(src, dst))
    os.symlink(src, dst)
# endif
