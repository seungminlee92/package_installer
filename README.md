# package_installer

This package allows python-users to install external-package easily with out command prompt.


# How to install

```
pip install package-installer
```

# How to use
```python
# example
from package_installer.installer import installer

# if package in pypl
result = installer("pandas")

# if package in git only
result = installer([pkg_nm]).git(
    git=[git_url],
    token=[token] # if necessary
)
```