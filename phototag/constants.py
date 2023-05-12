from pathlib import Path

# Root directory of the project
PROJECT_ROOT: Path = Path(__file__).parent.parent

# Extension Constants
RAW_EXTS = ["3fr", "ari", "arw", "bay", "braw", "crw", "cr2", "cr3", "cap", "data", "dcs", "dcr", "dng", "drf", "eip",
            "erf", "fff", "gpr", "iiq", "k25", "kdc", "mdc", "mef", "mos", "mrw", "nef", "nrw", "obm", "orf", "pef",
            "ptx", "pxn", "r3d", "raf", "raw", "rwl", "rw2", "rwz", "sr2", "srf", "srw", "tif", "x3f", ]
LOSSY_EXTS = ["jpeg", "jpg", "jpe", "png"]
