# `name` is the name of the package as used for `pip install package`
name = "package-name"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
version = "0.1.0"
author = "Author Name"
author_email = ""
description = ""  # summary
license = "MIT"
