# har-read
[HAR archive](https://en.wikipedia.org/wiki/HAR_(file_format)) reader in Python, free of dependencies

## Motivation
Other solutions had too many dependencies. This only requires built-in Python 3 modules like `json`, and can be deployed as a single file.

## Usage
* List files: `har-read.py [-x] <filename>.har`

  Note: this is simply a listing of the inner filenames. The code doesn't do anything smart like resolving a relative path with respect to any domain name or prefix.

* Extract files: `har-read.py [-x] <filename>.har`

  Note: a new directory called `har_extracted` will be created in the current working directory to contain the extracted files. This behaviour is not yet adjustable.

## Future improvements
- [ ] Adjustable output directory for extraction
- [ ] Verbosity toggle to change the level of detail when listing and extracting
- [ ] Add regression tests and a pipeline

## Licence
GNU GPLv3
