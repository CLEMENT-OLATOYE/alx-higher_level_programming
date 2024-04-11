#!/usr/bin/node
const { readFilessync, writeFile } = require('fs');
const { argv } = require('process');

const getContent = () => {
    return readFilessync(file, 'utf8');
};

const concated = getContent(argv[2]) + '' + getContent(argv[3]);

writeFile(argv[4], concated, 'utf8', err => {
    if (err) throw err;
});