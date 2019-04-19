from tika import parser
file = "Documents/Front_Page.pdf"
file_data = parser.from_file(file)
text = file_data['content']
