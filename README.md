# kep

Kep is a commend-line not taking and documenting tool.

## Goals

This project aims to achieve the following goals:

* Provide a list of CLI commands for taking notes
* Notes should open up in a text editor of choice, pre-formated, and only require a save action for them to be added to kep
* These commands should have shortcut commands for expediency
* `.kep` should be able to have an internal name that is different to their file name
* `.kep` files should be able to store a list of tags, and the tags should be searchable and filterable from the CLI
* `.kep` files should be able to be organized into folders, in addition to the tagging functionality
* `.kep` files should be able to reference non-.kep files in the same folder, such as images, html files, etc.
* kep should be usable from anywhere, but stores notes in a single place
* The location of the `/kep/` files directory should be configurable
* `.kep` files should be able to be printed/displayed in the CLI, separate from editing
* `.kep` files should be able to do minor mardown styling when reading
* The `/kep/` files directory should be navigable in the CLI, and properly store `.kep` files relative to the current location

## Folder Structure

By default, the expected folder structure of the `/kep/` directory will be:

```shell
/home/kep/
        .kep/
            index   # Stores an index of folders and tags for faster searching
            config
        notes/
            # List of subfolders and un-sorted .kep files
```

## File format

kep files should have a header that stores metadata information (such as for tagging, linking, etc), followed by the content.
All header fields are optional.

deploymentmeetingnotes.kep:
```yaml
Title: Software A Deployment Meeting Notes
Date Created: 2019-10-23 11:32 am
Date Modified: 2019-10-23 1:14 pm
Tags: notes software_a meeting october 2019
---

Brad didn't show up to this meeting, should remember to get with him later to review

- Stuff about scope
    * Some other stuff about scope
    * [Pdf in this same folder](scope.pdf)
- What it should look like
    * Colors and stuff

|---------------|
|               |
| Ascii Picture |
|               |
|---------------|
```

kep files can also contain only metadata and reference other files copied to the same directory.
This is useful for using kep to keep simple productivity scripts that you want to find later in a taggable format

copydatabase.sql.kep
```yaml
Title: Copy Database
Date Created: 2019-8-16 4:13 pm
Tags: sql database user copy sql_procedure scripts
Files: copydatabase.sql
---
```

## Current Usage

kep doesn't currently have any usable functionality.

## Planned Usage

Create a new note in the destination subdirectory under `/home/kep/files/`. Stores the note unsorted under `/files/` if no directory is given. Immediately opens the file in the default text editor or editor of choice specified in the config.

```shell
kep note "Software A Deployment Meeting Notes" /meetings
```

Can also take a .kep file name to keep it simple

```shell
kep note donuts.kep /thoughts/food
```

Shortcut for `kep note`. If the first argument has a slash in it, it is assumed that it is the destination for a file name

```shell
kep /meetings "Software A Deployment Follow Up"
```

Or just store the note in the default directory
```shell
kep "note i will sort later"
```

Copy a file to the kep `/files/` directory. For use outside of `/home/kep/`. Open the metadata `.kep` file for that file afterwards.

```shell
kep file websiteScrape.py /scripts/python
```

Print the contents (but not the metadata) of a `.kep` file to the console

```shell
kep read /meetings/deploymentmeetingnotes.kep
```

```shell
kep read /meetings/ "Software A Deployment Meeting Notes"
```

Search for files with given name

```
kep search deployment

> Notes with names containing 'deployment':
    1. "Software A Deployment Meeting"  /meetings/deploymentmeetingnotes.kep    2019-10-23
    2. "Website Deployment Meeting"     /meetings/websitemeetingnotes.kep       2018-11-05
    3. "deployment.py"                  /scripts/deployment.py.kep              2019-02-17
```

Search for files with given tag

```
kep search -tag meeting 2019

> Notes with tags 'meeting', '2019':
    1. "Software A Deployment Meeting"  /meetings/deploymentmeetingnotes.kep    2019-10-23
    2. "Software A Planning Meeting"    /meetings/deploymentmeetingnotes.kep    2019-10-16
```

Read a specified note from the previous search (dynamic!)

```shell
kep read 2
```

Same as `kep read`, but opens the .kep file in your editor of choice

```shell
kep edit <kep file or number if previously searched>
```

Tentative additional commands:

```shell
kep tags ...                                # show tags on given file
kep tag add ...                             # add tag to given file
kep file -fetch ...                         # copy file from /kep/files to current location
kep search -tag meeting -date < 2018-5-1    # search for files with the given tag created before 2019-5-1
```