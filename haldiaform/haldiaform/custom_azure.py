from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'aasif112' # Must be replaced by your <storage_account_name>
    account_key = 'hm7RrmN7dwUZvhDQ8dkdWmAdoDXmr8zEDmBKoSaUa/EeoTy1Uu7nzq0oucsTAVNNhP7G2wJuFICI+AStQC3khg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'aasif112' # Must be replaced by your storage_account_name
    account_key = 'hm7RrmN7dwUZvhDQ8dkdWmAdoDXmr8zEDmBKoSaUa/EeoTy1Uu7nzq0oucsTAVNNhP7G2wJuFICI+AStQC3khg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None