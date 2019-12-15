# djangoProject
1. When you Upload a file from the Front-end.It download the file in project directory and store its name in fileField.
2. The content of that file hashed into MD5 hash and stored in charField.
3. Now content of both Fields are stored into postgresql DB
4. on each DB save() operation a pre and post signal is generated via django signals and a log is created in log.txt
