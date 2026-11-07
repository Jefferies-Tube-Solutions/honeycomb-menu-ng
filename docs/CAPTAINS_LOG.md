# Captain’s Log

These entries record earlier releases. Linked guides use their current filenames.

[Complete Honeycomb Menu NG v1 release history](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/blob/25291186b07bfee81b8877fe731e00a417d56c12/RELEASE_NOTES.md)

Candidate reference: [v1.8 runtime namespace and mixed-install routing](NG_RUNTIME.md).
Stable v1.7.1 remains published and unchanged until separate owner approval.

The v1.8.0 candidate includes [40% active depth and decorative logo gradients](CUBE_PRESENTATION.md), [image-aligned `size: auto`](FLOORPLAN_SIZING.md), and an opt-in [six-sided energy pulse](ENERGY_WAVE.md). Inactive physical cubes remain solid. Numeric sizes and non-collapsible omitted fixed-82 defaults stay unchanged.

### Floorplan sizing in v1.8.0-beta.6

For a persistent Hub or Control inside `picture-elements`, opt in with
`size: auto`. A floorplan displayed at 50% of its reference design width gets
41px cubes; 75% gets61.5px. Reference defaults to1536 CSS pixels; set
`auto_reference_width` to your intended normal display width. Existing numeric sizes stay fixed. No detectable image
means a harmless 82px fallback. See [complete copy/paste YAML, coordinate-frame
support and touch-size limits](FLOORPLAN_SIZING.md).

The [synthetic charging-pulse demo](../examples/energy-wave.yaml) uses the shared
renderer without a charger or service call. Charger and Climate use this same renderer. [HACS listing readiness](HACS_SUBMISSION.md) is
separate from installing this stable release as a custom repository.

### v1.8.0-beta.6: corrected auto reference and power pulse speed

`size: auto` uses a stable **display/design reference width**, default1536 CSS
pixels. Use `auto_reference_width: 1500` for82px at a1500px displayed floorplan,
41px at750px. High-resolution source images no longer make cubes start tiny.
Current beta.4 caps normal auto sizing at 82px. Explicit numeric sizes remain
fixed; ordinary omitted size remains 82px, while Collapsible Hubs default to auto.
Read the
[complete floorplan YAML and migration](FLOORPLAN_SIZING.md).

The [power-speed demo](../examples/energy-wave-power.yaml) keeps true hexagonal
geometry and adds bounded power/fixed speed with phase-preserving smooth rate
changes. It requires no charger or service call. Existing energy_wave settings
retain their three-second cycle. [Rate settings and real sensor mapping](ENERGY_WAVE.md).
The owner-approved40% and logo gradients, native Sonos and other modules remain.

### v1.8.0-beta.7: energy-wave contour color (#119)

The scoped beta.6 follow-up makes the pulse inherit the cube's resolved inner
border, including live Light/Sonos colors and user overrides. Optional
`energy_wave.color: '#00bfff'` changes only the contour. Existing gradients,
six-sided geometry, power/fixed speed and sizing stay unchanged. Try the
[complete synthetic green/blue demo](../examples/energy-wave-color.yaml) and read
the [color and template rules](ENERGY_WAVE.md#contour-color--v180-beta7).
This setting starts in beta.7; published beta.6 remains immutable.


### Anchored child menus (v1.9.0-beta.4)

Opening a promoted child keeps the selected cube at its exact physical position;
it becomes that submenu's slot 0. Back restores the previous anchor and layout.
This also applies to deeper Charger/generic menus and responsive floorplans.
Light palettes/zoom and Sonos Radio/Join/Sleep retain their existing navigation.
In v1.9.0-beta.5, every ordinary submenu depth defaults to the same neutral gray
fill and inner border as Light controls; the dark outer border remains unchanged.
Charger details use that shared gray rather than a black fill. Root Hub base
fill/status styling and meaningful module/center/palette colors are preserved. Explicit
`colors.inner_border` overrides still win; the promoted center keeps its selected
appearance. Root status colors and intentional Light/Sonos colors are preserved.
