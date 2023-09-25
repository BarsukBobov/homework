try:
    open('database.sqlite')
except OSError:
   2/0

# try:
#     open('database.sqlite')
# except OSError:
#     raise ValueError("test1")

# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError("test2") from None

