# Ableton Live Object Model bridge

## Goal
Use Ableton's Live Object Model (LOM) as the primary control plane for AI-assisted production. GUI automation is a fallback only when a required operation is not exposed by Live or the plug-in.

## Supported access pattern
Max for Live can query, observe and control Live through `live.path`, `live.object`, `live.observer`, `live.remote~`, `live.modulate~`, or the Max JavaScript `LiveAPI` object.

A typical automatable plug-in parameter has a canonical path such as:

`live_set tracks N devices M parameters L`

The bridge should discover the actual objects at runtime rather than assuming fixed indexes.

## Discovery pass
Before any write action, collect at minimum:
- Live Set identity/session marker if available to the implementation.
- track id, track name, track type and canonical path.
- device id, device name, `class_name`, `class_display_name`, type and canonical path.
- each accessible automatable parameter: id, name, original_name, value, min, max, is_quantized, value_items, is_enabled, automation_state, display value if available.
- mixer volume, pan, sends and activator when relevant.
- rack/macro structure when relevant.

Only automatable Device parameters are exposed by the Device `parameters` child. Do not claim access to hidden/non-automatable controls unless another documented route exists.

## Read/write choices
### Persistent editing
For ordinary edits that should become part of the Live Set, prefer `live.object` / `LiveAPI` writes to `DeviceParameter.value`, with normal undo-aware workflow handled by the implementation.

### Realtime performance control
Use `live.remote~` only when true realtime/sample-accurate remote control is required. While a parameter is controlled by `live.remote~`, the parameter is disabled for direct editing/automation and the remote values do not become ordinary saved parameter edits. Release the remote mapping (`id 0`) after performance control.

### Modulation
Use `live.modulate~` when modulation semantics are intended rather than direct remote takeover.

## Live 12 conveniences
Live 12 can copy LOM paths for many objects from context menus, which is useful for debugging and manual verification.

As of Live 12.4.3, Max for Live can open/close plug-in editor windows via the LOM. Use this only as a fallback path for GUI-dependent operations; parameter-level control remains preferred.

## Device and preset handling
A `PluginDevice` can expose a preset list and selected preset index. Treat preset changes as high-impact state changes: verify the target device and, when possible, capture current state before changing.

## Stable targeting rule
Never identify a production target only by numeric indexes. Resolve using this priority:
1. persistent object id/path in the active Set when safe,
2. canonical track/device names defined by the studio template,
3. device class/display name,
4. semantic macro/parameter name,
5. current index only as a final runtime locator after verification.

## Verification after every write
Read the target back and confirm:
- the same object is still selected,
- parameter remains enabled,
- the value/display value matches the requested result within tolerance,
- automation state has not been unintentionally overridden,
- no protected low-end/master safety rule was violated.
