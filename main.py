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
    base_envrc = os.path.join(f"{BASE_DIR}/.", ".envrc")
    for root, dirs, files in os.walk(src_folder):
        if root.startswith(BASE_DIR):
            continue
        if ".envrc" in files:
            rel_path = os.path.relpath(root, src_folder)
            target_dir = os.path.join(BASE_DIR, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            envrc_target = os.path.join(target_dir, ".envrc")
            if envrc_target == base_envrc:
                print(f"==> skipping {envrc_target}") 
                continue
            shutil.copy(os.path.join(root, ".envrc"), envrc_target)



if __name__ == "__main__":
    app()
