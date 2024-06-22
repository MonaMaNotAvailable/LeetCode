#!/bin/bash

# This script counts the number of non-hidden files in each subdirectory and excludes the .git directory from the search.

# The `find` command is used to locate directories and count files.
# `-mindepth 1` ensures the current directory is excluded from the results.
# `-type d` specifies that we are looking for directories.
# `-name .git -prune` skips the .git directory.
# `-o` is the logical OR operator, allowing the continuation of the command.
# `-exec sh -c 'COMMAND' \;` executes a shell command for each directory found.

find . -mindepth 1 -type d -name .git -prune -o -type d -exec sh -c '

  # Inside the -exec, another find command is used to count files.
  # {} is the placeholder for the current directory being processed.
  # The inner find command:
  # `-maxdepth 1` ensures we only look at files in the current directory, not subdirectories.
  # `-type f` specifies that we are counting files.
  # `! -name ".*"` excludes hidden files (those starting with a dot).
  # wc -l counts the number of lines (i.e., the number of files found).
  # awk formats the output to display the directory name and file count.
  # removing the leading "./" from the directory name.
  # piped (|) to sort to arrange them in ascending order based on the count.
  # `-t:` specifies : as the field delimiter.
  # `-k2` sorts based on the second field (the count) and `-n` sorts numerically.

  find "{}" -maxdepth 1 -type f ! -name ".*" | wc -l | awk -v dir="{}" "{sub(/^.\//, \"\", dir); print dir \": \" \$1}"' \; | sort -t: -k2 -n