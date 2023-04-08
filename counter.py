
diff = None
with open('header.txt.patch', 'r') as f:
    diff = f.read()

diff_header, chunk_header, chunk = diff.split('@@')
