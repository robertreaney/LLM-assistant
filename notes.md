# Notes

I left off with the VSCode extension after exploring a little of the boilerplate provided by the docs.

## Files of interest
- `src/extension.ts`: contains the logic for actions performed by extension in the form of instantiation of vscode command classes that allow you to write "if action occurs here is the code to run"
- `package.json`: registers what the extension should expect to handle. `Commands` must be registered here to have the associated code in the `.ts` files to work correctly. This is also where you would outline `Views`, etc.

## How To
- Press F5 in this repo to build the extension
- That will pop open another vscode window with you "development" mode for your extension. This other window will allow you to interact with the current state of your repo (refresh with `Ctrl+r`).
- This works with debug breakpoints as well.