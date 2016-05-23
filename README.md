# btcde-passfile-reader

A python script for parsing a pdf file consisting of passwords provided by [Bitcoin.de](https://www.bitcoin.de) when enabled the two-factor authentication over a hashed password table.

## Usage

### Python 2.7
```
> btcde_validate2.py
```
### Python 3.x
```
> btcde_validate.py
```

-

### Example usage:
```
> btc_validate.py
> Code: B6 D2 A3 N8   <= Code received after logging in
> k p * 7             <= Answer code to be passed to bitcoin.de
```

Tested on Windows 7 and further.
For now, each Python major version has it's own script. Eventually I'll get back at some point and make them become one script compatible for both versions.
