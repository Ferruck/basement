from bob.errors import ParseError
import fnmatch
import os

# TODO: support more architectures; support musl/dietlibc

# get host architecture
def hostArch(args, **options):
    m = os.uname().machine
    if m == "x86_64":
        return m
    elif m.startswith("i"):
        return "i386"
    elif m.startswith("aarch64"):
        return "arm64"
    elif m.startswith("arm"):
        return "arm"
    else:
        raise ParseError("Unsupported host machine: " + m)

# get host autoconf triple
def hostAutoconf(args, **options):
    u = os.uname()
    if u.sysname != 'Linux':
        raise ParseError("Unsupported system: " + u.sysname)

    return u.machine + "-linux-gnu"

# set or replace vendor field in autoconf triplet
def genAutoconf(args, **options):
    if len(args) != 1:
        raise ParseError("$(gen-autoconf,vendor) expects one argument")
    u = os.uname()
    return u.machine + '-' + args[0] + '-linux-gnu'

manifest = {
    'apiVersion' : "0.15",
    'stringFunctions' : {
        "gen-autoconf" : genAutoconf,
        "host-arch" : hostArch,
        "host-autoconf" : hostAutoconf,
    }
}
