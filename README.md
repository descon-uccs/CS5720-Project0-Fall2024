# CS5720-Project0-Fall2024

To generate GPT-4o's attempt at CS 5720 Project 0, complete the following steps:

```shell
# clone this repo:
git clone https://github.com/descon-uccs/CS5720-Project0-Fall2024.git

# generate the figure files:
python second_code.py

# compile the PDF document (twice so it updates all the references)
pdflatex main.tex
pdflatex main.tex
```

This assumes you have a Python 3.x environment with numpy and matplotlib, and that you have LaTeX on your system with the required libraries.

The completed PDF is generated as `main.pdf`.

## Files
- ChatGPT.txt: the full chat transcript with GPT-4o.
- first_code.py: the first code GPT told me to write. This code doesn't export the figure files. This was made obsolete by the second Python prompt!
- main.txt: the LaTeX code GPT told me to write.
- second_code.py: after I asked for figure exports, this is the code GPT told me to write. This rendered the first Python file obsolete, and can be used stand-alone.
