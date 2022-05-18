# lst_utils

Small and hopefully soon to be expanding suite of tools for LST and others.

## Installation

```bash
git clone https://github.com/cloudyd3/lst-utils
cd lst-utils
pip install build
python -m build
pip install dist/lst_utils_cloudyd3-0.1.0-py3-none-any.whl
```

## Usage

```
disputes [-h] -s SOURCE -st SOURCE_TAB -d DESTINATION -dt
               DESTINATION_TAB [-c CREDENTIALS] [-i INDEX]

Filtering and formatting LST disputes

options:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source Google spreadsheet key
  -st SOURCE_TAB, --source_tab SOURCE_TAB
                        Source Google spreadsheet tab name
  -d DESTINATION, --destination DESTINATION
                        Destination Google spreadsheet key
  -dt DESTINATION_TAB, --destination_tab DESTINATION_TAB
                        Destination Google spreadsheet tab name
  -c CREDENTIALS, --credentials CREDENTIALS
                        Google credentials file
  -i INDEX, --index INDEX
                        Starting index
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/mit/)