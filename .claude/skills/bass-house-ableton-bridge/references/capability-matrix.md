# Capability Matrix — v18

Statuts : `UNKNOWN`, `SUPPORTED`, `UNSUPPORTED`, `PARTIAL`, `FAILED_TEST`.

| Capability key | Validation |
|---|---|
| `read_tracks_devices` | enumerate + readback |
| `ensure_track` | create or resolve a temporary named track, then verify |
| `create_clip` | temporary clip + length readback |
| `write_notes` | round-trip pitch/start/duration/velocity |
| `write_parameter` | set + readback |
| `serum_exposed_parameters` | host enumeration on current instance |
| `rack_macros` | macro enumeration + set/readback |
| `realtime_remote` | controlled live.remote~ test + release |
| `automation_persistent` | write/test/reload and verify envelope |
| `transport_observer` | start/stop/position events |
| `rollback` | snapshot + restore + readback |

Une capacité `SUPPORTED` doit stocker versions, méthode, date, limites et test de régression minimal. Les IDs LiveAPI sont toujours redécouverts dans la session courante.
