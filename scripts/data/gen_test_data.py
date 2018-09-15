#!/usr/bin/env python
import yaml

#
# Counselor file format is a yaml, structured as:
#
#
# - name: Person 1
#   loc: London, UK
#   mobile: +CC 0123456789 (text string)
#   availability:
#    - start: YYYY-MM-DD-hh:mm (datetime string)
#      end: YYYY-MM-DD-hh:mm
# - name: Person 2
# ...
#
