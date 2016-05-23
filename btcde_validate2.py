#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import PyPDF2

pdf_file_obj = open('Passworttabelle.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj, strict=False)
page_obj = pdf_reader.getPage(0)
tbl = {}

i = 0
current_row = 0
raw_table = iter(page_obj.extractText().encode('utf-8').strip())
for j, char in enumerate(raw_table):
	if 32 < ord(char) < 127:
		if i > 26: # skip header

			# blacklisted ids
			if j in [ 100, 106,
					  134, 136, 164, 170,
					  198, 200, 228, 234,
					  262, 264, 292, 298,
					  326, 328, 356, 362,
					  390, 392, 420, 426,
					  454, 456, 484, 490,
					  518, 520, 548, 554,
					  582, 584, 612, 618,
					  646, 648, 676, 682]:
				continue

			current_col = chr((i-1) % 26 + 65)
			current_row = (i-1) / 26
			if current_row == 10:
				current_row = 0
			elif current_row > 10:
				break # parsing done, get 'outta there

			tbl[current_col + str(current_row)] = char

		i += 1

assert i == 287, "Couldn't parse password table. Application will quit now."

args = raw_input('Code: ').split()

answer = []
for arg in args:
	answer.append(tbl[arg.upper()])
	
print ' '.join(answer)