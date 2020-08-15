#!/usr/bin/env python3
import os
import sys
import glob

def rm_file(f):
    if os.path.isfile(f) or os.path.islink(f):
        os.remove(f)
    # endif
# enddef

if __name__ == '__main__':
    resume_files = glob.glob1('resumes', '*.json')
    print('>> Select resume file.')
    for indx_t, res_file_t in enumerate(resume_files):
        print('{}. {}'.format(indx_t, res_file_t))
    # endfor
    res_file_no = int(input('>> Enter choice ? '))
    if res_file_no not in range(0, len(resume_files)):
        print('>> ERROR:: Choice should be between {} and {}'.format(0, len(resume_files)))
        sys.exit(-1)
    # endif

    theme_dirs = glob.glob1('themes', '*')
    print('>> Select theme.')
    for indx_t, tdir_t in enumerate(theme_dirs):
        print('{}. {}'.format(indx_t, tdir_t))
    # endfor
    tdir_no = int(input('>> Enter choice ? '))
    if tdir_no not in range(0, len(theme_dirs)):
        print('>> ERROR:: Choice should be between {} and {}'.format(0, len(theme_dirs)))
        sys.exit(-1)
    # endif

    theme_dir    = os.path.join('themes', theme_dirs[tdir_no])
    resume_json  = os.path.join('resumes', resume_files[res_file_no])

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
