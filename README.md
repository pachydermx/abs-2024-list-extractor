### Notes
This is a simple script using BeautifulSoup to extract ABS 2024 Journal list (i.e.,Academic Journal Guide 2024).
Please see the original interactive table at [charteredabs.org](https://charteredabs.org/academic-journal-guide/academic-journal-guide-2024)

### Instructions
- Install **BeautifulSoup** with the following command
```
pip3 install bs4
```

- Download **Rendered** pages under `tables` directory
- Run `capture.py` with the following command
```
python3 capture.py
```
- The script will capture tables of all files under `tables` directory, and save the result as `capture.csv`
- Enjoy

### Disclaimer
This repository contains code for educational and research purposes only. The scripts provided here are designed to assist in web scraping from publicly accessible sources. Users must comply with the terms of service of the websites they are scraping. This code is provided with the understanding that users will adhere to these terms.