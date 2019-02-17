# check-and-update

Automatically checks the Arch Linux website for new news items before running a system update.

## Dependencies:

Using this script requires you to have both python and Beautiful Soup installed.

```
pacman -S python
pacman -S python-beautifulsoup4
```

Alternatively Beautiful Soup can be installed with

```
pip install bs4
```

## Usage:

Simply execute the script using

```
./check-and-update
```

The first time it is run it will download a copy of the archlinux.org website. Each sucessive run the local copy of the site is compared with archlinux.org. If no new news items are found an update is performed with pacman, otherwise the user is advised to check the website before the next update and the local copy of the website if updated.

### Options:

```
	-n, --no-update     Do not run an update after checking website.
 	-c, --check-only   Check the website but do not save new copy.
 	-d, --dry-run      Same as -n and -c.
 	-p, --path [PATH]  Specify path to the local html file.
 	-u, --url [URL]    Specify the URL to check.
 	-h, --help         Display this help.

```
