from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'account-name' # Must be replaced by your <storage_account_name>
    account_key = 'account-key' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None
