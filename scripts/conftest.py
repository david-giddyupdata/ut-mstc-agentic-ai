# smoke_test.py is a setup check, not a test: stop pytest from collecting (and running) it.
collect_ignore = ["smoke_test.py"]
