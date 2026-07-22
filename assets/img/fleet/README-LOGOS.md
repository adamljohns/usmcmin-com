# Fleet agent logos — drop-in instructions

The dashboard shows a colored **monogram** for each agent until a real logo exists.
To use your Telegram logos, just drop a PNG here with the agent's id as the filename.
No code change, no rebuild step needed — the page picks it up automatically (the
monogram is an `onerror` fallback).

Recommended: square PNG, ~256×256, transparent or dark background.

| Drop this file | Agent |
|---|---|
| `main.png`         | Max Pemberton (Adjutant) |
| `hermes.png`       | Hermes (Staff Officer) |
| `cursor.png`       | Cursor Strike Team |
| `claude-meister.png` | Claude Meister |
| `preacher-john.png`| Preacher John |
| `chaps.png`        | Chaplain Chuck |
| `carnegie.png`     | Andrew Carnegie III |
| `sally.png`        | Sally Mae Thornton |
| `coach-arnie.png`  | Coach Arnold Briggs |
| `doc.png`          | Doc Hartley |
| `sheriff-roy.png`  | Sheriff Roy Caldwell |
| `prof-x.png`       | Professor Xavier |
| `rush.png`         | Rush Sullivan |
| `pops.png`         | Pops Henderson |
| `sgt-maj-mac.png`  | SgtMaj Mac McAllister |
| `bg-hartwell.png`  | BG Gus Hartwell |

After dropping the files: `git add assets/img/fleet && git commit -m "fleet: agent logos" && git push`
(or just let the next auto-refresh pick them up — but it only commits on state change,
so a manual commit is the reliable way to publish new logos.)
