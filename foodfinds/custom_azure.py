from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'foodfinds' # Must be replaced by your <storage_account_name>
    account_key = '4/FNPwIaeKfW11VguGacYw5emNxLy5/MjwP8Tg+Hc4cHo7ooov16t42x+A30Gj1YhsOpZjYqV9gv9YjpIAzMiw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None