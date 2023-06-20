# OAB Records PDF Searcher (Python)

This Python script is designed to search for records from the Brazilian Bar Association (OAB) within PDF files. It provides an automated way to extract relevant information such as registration numbers and lawyer names from the PDF files.

## Features

- Search for OAB records within PDF files
- Extract registration numbers and associated information
- Automate the search and extraction process

## Requirements

- Python 3.x
- Python Libraries: [list the required libraries]

## Usage

1. Instale as dependências necessárias:
```shell
pip install -r requirements.txt
```

2. Run the script by providing the path to the PDF file:
```shell
python src/main.py oab_records="16537-A/AL,133921/SP,154467-A/RJ,46843-A/RJ"
```

3. After the search is completed, the script generates an XLSX table as output containing the extracted information.

4. View the generated XLSX table to access the extracted OAB records.

## Contribution

Contributions are welcome! If you encounter issues or have improvements to suggest, feel free to open an issue or submit a pull request.

## Limitations

- The script currently supports only PDF files formatted in a specific way.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



