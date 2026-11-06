# Jefferies Navigation runtime API v2

The runtime is available at `window.jefferiesNavigation`. It exposes
`apiVersion === 2`, `version` and `commit`. Dashboard cards register
`jts-n-hub` and `jts-n-control`. The popup, menu cell, Info Cube and XY Pad use
the same `jts-n-` namespace.

```js
const navigation = window.jefferiesNavigation;
navigation.open({ entity: 'light.room_a', buttons: [] });
navigation.back();
navigation.close();
```

Persistent owners can create a private context and call `openInContext`,
`updateBase`, `backInContext`, `closeInContext` and `disposeContext`. A
context owns its scene, navigation stack, gestures, pending actions and Info
overlay. Dispose it when the owner is detached.

External `fire-dom-event` payloads use `jts_n_menu` or `jts_n_info`. Templates
live under `jts_n_menu_templates` in dashboard YAML. See [the migration table](V2_MIGRATION.md)
for the previous names and [Info Cube](INFO_CUBE.md) for configuration.

The browser coexistence test loads the pinned original Honeycomb resource by
itself, JTS-N by itself, and both in both orders on desktop and mobile. It
checks that popup events, the runtime namespace and custom elements are independent.
