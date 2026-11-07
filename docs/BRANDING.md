# Jefferies Navigation branding

Jefferies Navigation (JTS-N) uses the JTS publisher identity in its public README
and the Navigation compass in Home Assistant. The public repository slug is
`Jefferies-Tube-Solutions/jefferies-navigation`. During the rename, GitHub
workflows use the repository that started the run. Historical release references
and the original author's GPL attribution retain their original identity.

Follow the JTS Brand System v1.1.0 policies for README hierarchy and theme
variants, documentation, Home Assistant applicability, and release status.
[Canonical brand policy](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/docs/README_LAYOUT.md).

| Use | Source | Preview |
| --- | --- | --- |
| Publisher, GitHub dark theme | [Tunnel 06 / Layout 02, white text](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/jts/v4/jts-white-transparent.png) | <img src="../assets/brand/jts-white-transparent.png" width="160" alt="JTS publisher mark, white text"> |
| Publisher, GitHub light theme | [Tunnel 06 / Layout 02, Deep Space text](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/jts/v4/jts-deep-space-transparent.png) | <img src="../assets/brand/jts-deep-space-transparent.png" width="160" alt="JTS publisher mark, Deep Space text"> |
| Product insignia, public documentation | [Navigation Draft 02 icon](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/products/jefferies-navigation/v1/JTS_Jefferies_Navigation_Icon.png) | <img src="../assets/brand/jefferies-navigation-icon.png" width="100" alt="Navigation compass in the product hexagonal frame"> |
| Runtime compass, inside a Home Assistant cell | Draft 02 Blender dial collection | <img src="../assets/navigation-compass.png" width="100" alt="Round compass dial with cyan bezel and amber needle"> |

The public PNG copies preserve the approved pixel and color data. Export
comments and metadata with local authoring paths were removed. The runtime
compass was rendered from `Jefferies Navigation - Blender draft 02.blend`
(SHA-256 `0dc41d483c4fcd15ba5287be2f44e93f01356770188b219749ff4b83f6c5d3b2`)
in Blender 5.2.3 LTS. Render the `NAVIGATION / Editable compass` collection with
the original camera and lights, hiding all other geometry. Set the camera to
73 mm and render a transparent, 192×192 RGBA PNG. The renderer supplies the outer
hexagon. The product insignia retains its approved frame in public documentation.

Run `npm run check:brand` after any artwork or identity edit. The check pins
the current public PNG hashes and verifies package, HACS, release, runtime and
README identity. The existing core suite runs this check in CI and release
verification. When artwork or identity changes with owner approval, record the
exact source and approval, update the hashes and verify both GitHub themes and
the Home Assistant compass at supported sizes.
