import cx_Freeze

executables = [cx_Freeze.Executable (script="game.py", icon="assets/book3.png")]

cx_Freeze.setup(
    nome="Game Educacional Do Castelani",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
        }},
    executables=executables
)
