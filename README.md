## Before you start

1 Install venv and activate it

```bash
python -m virtualenv venv
python3 -m venv <nome-ambiente> # ubuntu 24.04, before install python-pip and python3-venv
source venv/bin/activate # for linux
venv\Scripts\activate # for windows
```

2 Install the requirements

```bash
pip install -r requirements.txt
```

3 Put all your links in the `links.txt` file

```txt
https://www.youtube.com/watch?v=...
https://www.youtube.com/watch?v=...
```

4 Run the script

```bash
python -m main
```

5 Get Packages Versions with Freeze

```bash
pip freeze > requirements.txt
```