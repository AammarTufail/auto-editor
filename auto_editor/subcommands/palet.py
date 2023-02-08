from __future__ import annotations

import sys

from auto_editor.interpreter import Interpreter, Lexer, MyError, Parser, env

def main(sys_args: list[str] = sys.argv[1:]) -> None:
    if sys_args:
        with open(sys_args[0], "r") as file:
            program_text = file.read()

        try:
            Interpreter(env, Parser(Lexer(program_text))).interpret()
        except (MyError, ZeroDivisionError) as e:
            print(f"error: {e}", file=sys.stderr)

    else:
        from .repl import main
        main(sys_args)

if __name__ == "__main__":
    main()
