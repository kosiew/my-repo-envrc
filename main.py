import typer
import os
import shutil

BASE_DIR = os.path.dirname(__file__)
app = typer.Typer()


# Setup the helper default
@app.callback(invoke_without_command=True)
def helper(ctx: typer.Context):
    """
    Awesome CLI app
    """
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())

@app.command()
def copy_envrc(src_folder: str):
    """
    Scans subfolders for .envrc and copies them under BASE_DIR.
    """
    for root, dirs, files in os.walk(src_folder):
        if ".envrc" in files:
            rel_path = os.path.relpath(root, src_folder)
            target_dir = os.path.join(BASE_DIR, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            shutil.copy(os.path.join(root, ".envrc"), target_dir)

def main():
    print("Hello from my-repo-envrc!")


if __name__ == "__main__":
    app()
