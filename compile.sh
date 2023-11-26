#!/bin/bash

cd src
eval $(opam env)
make all
make clean
mv papers.html ../papers.html
mv main.pdf ../assets/docs/JonahTHansenCV.pdf