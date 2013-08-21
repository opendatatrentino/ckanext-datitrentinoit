#!/bin/sh

# For LESS you can use:
# lessc ./less/datitrentinoit.less > ./datitrentinoit.css

# For SCSS use:
# scss -tcompressed -C --compass ./scss/datitrentinoit.scss > ./datitrentinoit.css

set -v
lessc ./less/datitrentinoit.less > ./datitrentinoit.css
