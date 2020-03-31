############################
############################
## Functinos to load Fasta
from itertools import groupby


#####################################################


def fasta_iter_raw(fasta_name):
    """
    Return iterator for fasta
    """
    fh = open(fasta_name)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    
    for header in faiter:
        # drop the ">"
        headerStr = header.__next__()   #[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s for s in faiter.__next__())  # .strip()
        yield (headerStr, seq) 
        
def fasta_iter(fasta_name):
    """
    Return iterator for fasta
    """
    "first open the file outside "
    fh = open(fasta_name)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))

    for header in faiter:
        # drop the ">"
        headerStr = header.__next__()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq) 
