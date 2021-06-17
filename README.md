[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2196331b2d82440c97dec358e74eb18a)](https://app.codacy.com/gh/JoshuaSBrown/PyCGADExample?utm_source=github.com&utm_medium=referral&utm_content=JoshuaSBrown/PyCGADExample&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://www.travis-ci.com/JoshuaSBrown/Py-CGAD_Example.svg?branch=main)](https://www.travis-ci.com/JoshuaSBrown/Py-CGAD_Example)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6Ikpvc2h1YVNCcm93biIsInJlcG8xIjoiUHktQ0dBRF9FeGFtcGxlIiwiaW5jbHVkZUxpbnQiOmZhbHNlLCJhdXRob3JJZCI6MTYzMDEsImlhdCI6MTYyMjMyMjk2Nn0.8AscZ13QsImqUk1v1fA87GLRVe1Ww_UxnUoOQ3SwhlU)](https://www.deepcode.ai/app/gh/JoshuaSBrown/Py-CGAD_Example/_/dashboard?utm_content=gh%2FJoshuaSBrown%2FPy-CGAD_Example)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/13fb2c82625e498788eb63d06020eb7b)](https://www.codacy.com/gh/JoshuaSBrown/Py-CGAD_Example/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JoshuaSBrown/Py-CGAD_Example&amp;utm_campaign=Badge_Grade)

# PyCGADExample

Shows a concrete implementation of Py-CGAD. The post status script is a simple
script that allows you to post the status of a given task to each commit. It
is setup in this case within the ci.

To test it:

```Bash
python3 -m pytest
```

To see tests with printed output:

```Bash
python3 -m pytest -s
```

To run the post_status.py script:

```Bash
PYTHONPATH=$PYTHONPATH:status python3 ./bin/post_status.py --help
```

For more documentation see the wiki.
