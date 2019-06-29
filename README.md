# pathlinker
## Interactive Python script that substitutes files and folders with symbolic links

`pathlinker` moves files and folders from `original_dir` to corresponding subdirectories in `destination_dir` and adds the appropriate symbolic links to `original_dir`

* `original_dir` = directory with original files to substitute with symbolic links
* `destination_dir` = directory to store original files
* `tracked_paths` = paths in `original_dir` to substitute with symbolic links

# Setup

* move example `.pathlinker.json` settings  file to home directory (default settings file)
* change `original_dir`, `destination_dir` and `tracked_paths` as desired
* run `pathlinker`
* check `pathlinker --help` for information

# Testing

* run `./pathlinker_test.py`
