
# UV / UVX

Setup a virtual environment, but also get some of the MCP servers

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# NPX

Many of the MCP servers used (e.g. filesystem) are just yolo installed from the internet

```
sudo apt install nodejs npm
```

# GO

Some of the mcp servers depend on go binaries (zoekt)

```
sudo apt install golang-go
```

# Zoekt

```
go install github.com/sourcegraph/zoekt/cmd/zoekt-git-index@latest
go install github.com/sourcegraph/zoekt/cmd/zoekt@latest

~/go/bin/zoekt-git-index -incremental=0 -index .zoekt .
~/go/bin/zoekt -index_dir .zoekt/ mcp
```