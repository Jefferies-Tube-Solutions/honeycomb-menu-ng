# One shared Honeycomb Bee

The standard Hub Bee and expanded Collapsible Hub Bee use one preset, canonical
mascot, fill/borders, dimensions, animation and installed-version renderer.
No new YAML is needed. The optional expanded Bee center is:

```yaml
collapsible:
  expanded_center: bee
  primary_slot: 1
```

| Context | Short tap / Enter / Space | Hold / Shift+Enter / Shift+Space |
| --- | --- | --- |
| Standard branded Bee | Reveal installed version | Reveal installed version |
| Expanded root Bee | Back / Collapse | Reveal installed version without collapse |

The label is derived from actual build/release metadata, e.g. **v1.10.0 beta 8**.
It remains readable for three seconds; flight motion itself lasts 430ms. Repeated
inspection restarts one reveal window. Reduced-motion users retain the label
without flight. Detach cancels timers/frames. A hold never also triggers collapse
or the primary room action. Keyboard users can also use Alt+V on a Bee icon.

Explicit colors, backgrounds, borders and gradients remain supported. Functional
generic controls that happen to use a Bee icon retain their module semantics
and configured actions/styles; Alt+V makes the shared version available without
replacing those actions. A generic fallback icon is not a decorative status-free
Hub logo. Radio, Climate and other module appearances are unchanged.

## Optional rendered-size diagnostics

Top-level Hub `size_debug: true` adds one temporary line during version inspection:

```yaml
size_debug: true
```

Default is false; omitted/false has exactly the ordinary version-only reveal,
resting appearance, animation and gestures. No per-module YAML is needed. The Hub
opt-in follows all Bee instances in its navigation context, including expanded
Bee center and generic Bee icons. The common version formatter and renderer remain
shared. For beta.8 an automatic expanded Bee can show:

```text
v1.10.0
beta 8
82 px
```

The value comes directly from the rendered visible hex SVG bounding rectangle in
CSS pixels. It includes applicable transforms/scale and never substitutes configured
size, expanded_size, menu width or physical device pixels. Values use whole pixels
or one decimal (for example `79.4 px`); missing geometry says `N/A`.
Measurement runs on reveal and resize/ancestor-style events while visible, without
polling; observers/listeners/queued measurement frames are removed on hide/detach.
The accessible live status includes the measured size only in debug mode. Debug
uses compact three-line typography within the hex; standard version-only typography
is unchanged. Version reveal stays temporary for three seconds.

The diagnostic does not change the size policy: auto/omitted Hub maximum is 82px,
numeric size N is authoritative, and expanded_size may only lower that target.
The geometry engine and every child renderer use the same context ceiling.

## Future mascot replacement

Replace only `assets/honeycomb-bee.png`, then run `npm run prepare:brand` and the
normal build. `scripts/generate-bee-asset.js` generates the embedded derivative
`src/brand/bee.generated.js`. Do not hand-edit or duplicate that derivative.
`src/core/bee.js` owns shared preset/tokens, asset reference and version metadata;
`src/cube-element.js` remains the single renderer and gesture/animation owner.
The existing `src/core/version-label.js` remains the only version formatter.

A new Bee artwork is outside beta.8. Broad cleanup/review in issue #154
remains deferred until owner layout acceptance. Automated screenshots with
synthetic HA are separate from owner physical Android/PC acceptance.
