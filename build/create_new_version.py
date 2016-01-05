#!/usr/local/bin/python

def bump_version():
    f = open('version.txt', 'a+')
    f.seek(0)
    all_versions = f.read()
    if all_versions is '':
        return 1
    versions = all_versions.split('\n')[:-1]
    max = 0
    # This is on only for 9.3 versions.
    for v in versions:
        suffix = int(v.split('9.3.')[-1])
        if suffix > max:
            max = suffix
    version = '9.3.' + str(max + 1)
    f.write(version)
    f.close()
    return version

if __name__ == '__main__':
    bump_version()

