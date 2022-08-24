# package_installer

This package allows python-users to install external-package easily with out command prompt.


# How to install

```
pip install python-package-installer
```

# How to use
```python
# example
from py_package_installer import installer

# if package in pypi
result = installer("pandas")

# if package in git only
result = installer([pkg_nm]).git(
    git=[git_url],
    token=[token] # if necessary
)
```
