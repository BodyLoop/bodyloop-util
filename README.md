# bodyloop-dashboards

Several dashboards for exploring and visualizing [BodyLoop](http://bodyloop.life) data.

## Installation guide

### Prerequisites

- [uv](https://docs.astral.sh/uv/)

### One-shot run

You can use `uvx` to run the tool without installing it:

```bash
uvx --refresh https://github.com/bodyloop/bodyloop-dashboards/archive/refs/heads/main.zip
```

### Install locally

Install the tool with:

```bash
uv tool install --refresh https://github.com/bodyloop/bodyloop-dashboards/archive/refs/heads/main.zip
```

Run the tool with:

```bash
bodyloop-dashboards
```

### Creating an editable install

1. Clone the repository.
2. Sync dependencies:

```bash
uv sync
```

1. Run the CLI:

```bash
uv run bodyloop-dashboards
```

## CLI usage

After installing dependencies/syncing the project, run:

- `bodyloop-dashboards`

## Contribution guide

Contributions are welcome.

1. Fork or clone this repository.
2. Create a feature branch.
3. Install dependencies with `uv sync`.
4. Make your changes.
5. Verify the CLI still works, for example: `uv run bodyloop-dashboards`
6. Commit with a clear message and open a pull request.
