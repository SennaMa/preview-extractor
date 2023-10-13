# preview-extractor
### What
Extract highlighted and annotated text from Preview.

### How
1. Activate the virtual env and double-check that the venv was set up properly by running `which python3`.
`deactivate` when you're done.

```
source bin/activate
which python3
```

2. Install requirements
```
pip3 install -r requirements.txt
```

3. Run `main.py` to start the app.
```
python3 extractor/app/main.py
```

If you're running into: `RuntimeError: Directory 'static/' does not exist` then uninstall `fitz` and install `pymupdf`.
