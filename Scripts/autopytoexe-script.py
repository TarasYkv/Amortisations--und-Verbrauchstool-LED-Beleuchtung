#!C:\taras\neu2\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'auto-py-to-exe==2.6.6','console_scripts','autopytoexe'
__requires__ = 'auto-py-to-exe==2.6.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('auto-py-to-exe==2.6.6', 'console_scripts', 'autopytoexe')()
    )
