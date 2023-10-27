## Use it to add margin to pdf

I want to take notes on the pdfs, however the files have a small margin,
use this file to add margin to your pdf files.

## Usage

*add margin 30 on the input.pdf*
`python3 addmargin.py -f input.pdf -m 50`

**OR you can copy the file to `/usr/local/bin/`**

```python
cp addmargin.py /usr/local/bin/
cd /usr/local/bin/
chmod a+x addmargin.py
```

### Then use as follow

```python
# goes into the pdf folder
cd /path/to/pdf
addmargin.py -f your.pdf -m 30

```

If you found useful, make a star to me!!! Thank you.