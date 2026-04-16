# Calendar Prototype

This is a quick, single-page public calendar prototype.

## Files

- `index.html` — UI and client-side rendering logic
- `events.sample.json` — sample event feed

## Run

### Option 1: Open directly

Open `index.html` in a browser.

- The page attempts to load `events.sample.json`.
- If browser file security blocks `fetch` on local files, the page automatically falls back to embedded sample data.

### Option 2: Serve locally (recommended)

From repo root:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/prototype/
```

## Review checklist

- Events appear nearest-first
- Cancelled events remain visible and clearly marked
- Invalid Meetup URLs show disabled action text (and log a warning)
- Remove all items in `events.sample.json` to verify the empty state: `No upcoming events.`
