import onlinebrief24

with onlinebrief24.Client('<username>', '<password>', host='localhost', upload_path='<upload_path>') as c:
    c.upload('/tmp/file1.pdf', duplex=False, color=False, distribution='auto', envelope='din_lang')
    c.upload('/tmp/file2.pdf')
