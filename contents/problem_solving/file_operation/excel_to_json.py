from zipfile import ZipFile
from bs4 import BeautifulSoup
import pandas as pd


def excel_to_json(input_file_path=None, output_dir_path=None):
	"""Function to convert excel to json"""
	try:
		with ZipFile(input_file_path) as zipped_file:
		    summary = zipped_file.open(r'xl/workbook.xml').read()
		soup = BeautifulSoup(summary, "xml")
		sheets = [sheet.get("name") for sheet in soup.find_all("sheet")]
		for sheet in sheets:
		    df = pd.read_excel(file, sheet_name = sheet)
		    if sheet == 'sheet1':
		    	df['date_col'] = df['col1'].dt.strftime('%Y-%m-%d')
		    json_file = df.to_json(("{}.json").format(sheet), orient='records', date_format='iso')
		return True
	except Exception as e:
		print(e)
		return False


if __name__ == '__main__':
	file = 'example.xlsx'
	print(excel_to_json(file))