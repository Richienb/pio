# PIO

A simplified, yarn-like alternative to pip.

## Installation

```sh
pip install pio
```

## Usage

```sh
pio add example # Install example package
pio remove example # Remove example package
pio upgrade example # Upgrade example package (leave blank to upgrade all)
pio install # Install all packages from pio.json
```

## Migrate from `requirements.txt`

```sh
pio migrate requirements.txt
```

## Programmatic usage

```python
import pio # Import PIO package
pio.add("example") # Install example package
pio.remove("example") # Remove example package
pio.upgrade("example") # Upgrade example package (leave blank to upgrade all)
pio.install() # Install all packages from pio.json
```
