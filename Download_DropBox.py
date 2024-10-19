import dropbox

# Replace with your access token
ACCESS_TOKEN = 'sl.B_FiErGoCqHp6wWzxc8848XWJMwcp-C6m0GkZ0qe_ds669HXKm3AY86UOAJrxYhQHHq1AcjAggPt2vwhHqvqdbXSJlED9ECShaoaV5QDj4HHQieztB3KKfjjss5nZRfubmUFE48gM6zq'
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload_file(local_path, dropbox_path):
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path)

# Example usage
upload_file('/home/file', 'Linux')
