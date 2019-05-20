#!/bin/bash

exec jupyter-notebook --ip="*" --no-browser --allow-root &
exec service nginx start