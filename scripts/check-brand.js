'use strict';

const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const repository = 'Jefferies-Tube-Solutions/jefferies-navigation';
const artwork = Object.freeze({
    'assets/brand/jts-white-transparent.png': '0916cac2d9ffacc77369f2e36784c47a08ebb3861bc2edeea85debec0af81f4c',
    'assets/brand/jts-deep-space-transparent.png': 'e7a62fefd63df7f3a1e5c36ea4284765cd25059a3496454eac1d5ea28ffcd527',
    'assets/brand/jefferies-navigation-icon.png': '2e41949ceac68fb6315b2f1cae44ca24c194c6fa8bac66ea21b35c24644495f9',
    'assets/navigation-compass.png': '793f2f612bf899de6847b497719d51a9ac7ef38c7f8b6bbe7517e717c7257040'
});

function readBrand() {
    const read = file => fs.readFileSync(path.join(__dirname, '..', file));
    return {
        package: JSON.parse(read('package.json')),
        hacs: JSON.parse(read('hacs.json')),
        release: JSON.parse(read('release.json')),
        runtime: read('src/runtime.js').toString('utf8'),
        readme: read('README.md').toString('utf8'),
        artwork: Object.fromEntries(Object.keys(artwork).map(file => [
            file, crypto.createHash('sha256').update(read(file)).digest('hex')
        ]))
    };
}

function validateBrand(brand) {
    assert.equal(brand.package.name, 'jefferies-navigation', 'Unexpected package identity');
    assert.equal(brand.package.repository.url, 'git+https://github.com/' + repository + '.git', 'Unexpected repository identity');
    assert.equal(brand.hacs.name, 'Jefferies Navigation', 'Unexpected HACS name');
    assert.equal(brand.hacs.filename, 'jefferies-navigation.js', 'Unexpected HACS bundle name');
    const title = 'Jefferies Navigation v' + brand.package.version;
    assert.ok(brand.release.title === title || brand.release.title.startsWith(title + ' — '), 'Unexpected release identity');
    assert.match(brand.runtime, /window\.jefferiesNavigation\s*=/, 'Unexpected runtime identity');

    for (const [file, hash] of Object.entries(artwork)) {
        assert.equal(brand.artwork[file], hash, 'Unapproved artwork bytes for ' + file);
    }

    const sections = [
        '<p align="right">',
        'img.shields.io/github/v/release/' + repository,
        'assets/brand/jts-white-transparent.png#gh-dark-mode-only',
        'assets/brand/jts-deep-space-transparent.png#gh-light-mode-only',
        'assets/brand/jefferies-navigation-icon.png',
        '# Jefferies Navigation for Home Assistant'
    ];
    let offset = -1;
    for (const section of sections) {
        const index = brand.readme.indexOf(section);
        assert.ok(index > offset, 'README branding element missing or out of order: ' + section);
        offset = index;
    }
    for (const type of ['navigation-hub', 'navigation-control']) {
        assert.match(brand.readme, new RegExp('^type: custom:' + type + '$', 'm'),
            'README example must use custom:' + type);
    }
    assert.match(brand.readme, /\[.*\]\(docs\/AI_SETUP\.md\)/, 'README must link the AI setup guide');
}

module.exports = {readBrand, validateBrand};

if (require.main === module) {
    validateBrand(readBrand());
    console.log('JTS-N artwork and product identity verified.');
}
