Unzip a zip archive with files stored in Shift-JIS encoding on
non-Japanese systems.

## Usage

Japanese versions of Windows (and maybe other systems as well) still use
Shift-JIS encoding to store file names. When a zip file is created from
files with Japanese names on such a machine and then later opened on a
non-Japanese system (Windows, OS X or Linux), the file names are
garbled. This script unzips the file while converting the file names
from Shift-JIS to UTF-8.

```bash
python unzip-jp.py archive.zip
```

The above command creates a directory `archive` and unzips the content
of the archive `archive.zip` there.

I recommend making `unzip-jp.py` executable and simlinking it to
`unzip-jp`, and putting it in your `PATH`:

```bash
chmod +x unzip-jp.py
ln -s $PWD/unzip-jp.py ~/bin/unzip-jp
```

Then you can call it as

```bash
unzip-jp archive.zip
```

## Requirements

The script should work with [Python 2 and 3](https://www.python.org/).

## License

MIT license. See `LICENSE` for details.
