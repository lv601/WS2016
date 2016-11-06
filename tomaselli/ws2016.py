import io
import time
import re
from pprint import pprint




def parse_fasta(file_name):
    db = []
    try:
        isinstance(file_name.read(0), (bytes, bytearray))
        #  Instanz:
        #  isinstance(object, classinfo) Return true if the object argument is an instance of the classinfo argument
        for line in file_name:
            if line[0] == 62:
                ident, desc = line[1:].strip().split(maxsplit=1)
                db.append({'id': ident, 'description': desc, 'sequence': bytearray(), 'raw': bytearray(line)})
            else:
                db[-1]['sequence'] += (line.rstrip())
                db[-1]['raw'] += (line)
        print(db)
        return db
    except TypeError:
        print("Stream must be binary")


"""
          
open(name[, mode[, buffering]])
### Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode

Open a file, returning an object of the file type described in section File Objects. 
If the file cannot be opened, IOError is raised. When opening a file, it’s preferable to use open() instead of 
invoking the file constructor directly.

The first two arguments are the same as for stdio‘s f open(): name is the file name to be opened, 
and mode is a string indicating how the file is to be opened.

The most commonly-used values of mode are 'r' for reading, 'w' 
for writing (truncating the file if it already exists), and 'a' for appending 
(which on some Unix systems means that all writes append to the end of the file regardless of the 
current seek position). If mode is omitted, it defaults to 'r'. The default is to use text mode,
which may convert '\n' characters to a platform-specific representation on writing and back on reading.
  
Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode, 
which will improve portability. (Appending 'b' is useful even on systems that don’t treat binary and text files differently, 
where it serves as documentation.) See below for more possible values of mode.

The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered, 
1 means line buffered, any other positive value means use a buffer of (approximately) that size (in bytes). 
A negative buffering means to use the system default, which is usually line buffered for tty devices and 
fully buffered for other files. If omitted, the system default is used. [2]


"""
