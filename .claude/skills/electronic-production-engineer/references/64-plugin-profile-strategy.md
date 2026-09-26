# Plug-in profile strategy

## Purpose
A profile teaches the bridge how a specific instrument/effect maps to the common semantic vocabulary without hard-coding fragile numeric indexes.

## Profile identity
A profile should include:
- vendor
- product
- plug-in format when relevant
- detected class/display name
- profile version
- optional plug-in version range
- semantic mappings by parameter name/original name and optional stable parameter identity supplied by the implementation
- safe ranges / protected controls
- notes about quantized values

## Priority in this studio
Profiles worth building first:
1. Serum 2
2. Komplete Kontrol
3. Maschine 3 plug-in
4. FabFilter Pro-Q 4
5. FabFilter Pro-C 3
6. soothe3
7. Waves L4
8. Waves F6
9. Waves API 2500 / SSL G-Master
10. Waves R-Bass / MaxxBass
11. Analog Obsession RazorClip / TheBus
12. Ableton native Racks/devices used in the template

## Profile learning workflow
1. Load one plug-in instance in a safe test Set.
2. Discover all accessible parameters.
3. Match only high-confidence semantic targets.
4. Exercise each mapped control through a small range and verify the visible/audible result.
5. Save the mapping profile.
6. Revalidate after plug-in updates.

## Komplete Kontrol / NKS
NKS is useful as a semantic browsing and pre-mapping layer but is not treated as the bridge API. Prefer parameters exposed by Ableton/LOM. Do not reverse-engineer NKS files as the primary control strategy.

## GUI fallback
If a required plug-in function is not exposed as an automatable parameter, the bridge may return a `gui_fallback` action. The implementation should open the plug-in editor (where supported), perform the minimum GUI operation, then re-scan exposed state when possible.
