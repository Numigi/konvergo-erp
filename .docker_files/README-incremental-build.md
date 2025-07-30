# Incremental Gitoo Build Setup

This setup splits gitoo.yml into separate configuration files to enable incremental Docker builds. When you modify repositories in gitoo.yml, Docker will only rebuild the affected stages.

## How it works

1. **OCA Stage** (`gitoo-oca.yml`): All OCA repositories
2. **Numigi Stage** (`gitoo-numigi.yml`): All Numigi repositories  
3. **Final Stage**: Combines modules from both stages

## Benefits

- **Faster builds**: Only changed repository groups are rebuilt
- **Better caching**: Docker layers are cached per repository group
- **Reduced bandwidth**: Only download changed repositories

## Usage

### Automatic sync (recommended)
Run this script whenever you modify gitoo.yml:
```bash
python3 .docker_files/split-gitoo-config.py gitoo.yml
```

### Manual maintenance
If you add/remove repositories in gitoo.yml, update the corresponding:
- `gitoo-oca.yml` for OCA repositories
- `gitoo-numigi.yml` for Numigi repositories

## Build behavior

- **Change OCA repos only**: Only `oca-stage` rebuilds
- **Change Numigi repos only**: Only `numigi-stage` rebuilds  
- **Change both**: Both stages rebuild
- **No gitoo changes**: All stages use cached layers

## Example scenarios

1. Add new OCA repo → Only OCA stage rebuilds
2. Remove Numigi repo → Only Numigi stage rebuilds
3. Change Python deps → Final stage rebuilds, gitoo stages cached
4. No changes → Entire build uses cache