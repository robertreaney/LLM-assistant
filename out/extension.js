"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
const child_process_1 = require("child_process");
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
function activate(context) {
    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "llm-assistant" is now active!');
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('llm-assistant.generateCode', () => {
        // The code you place here will be executed every time your command is executed
        // Display a message box to the user
        // vscode.window.showWarningMessage('Here is some code!');
        // const text = process.env.OPEN_API_KEY;
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            // get selected text
            // TODO make this python call into an executable
            var pythonCommand = new String("C:/Users/kayla/Documents/Rob/LLM-assistant/dist/ext_entrypoint.exe -i ");
            const buffer = new String(' "');
            var selectedText = new String(editor.document.getText(editor.selection));
            const end = new String('"');
            vscode.window.showInformationMessage('Querying Model...');
            // send selected text to python to get LLM response
            (0, child_process_1.exec)(pythonCommand.concat(buffer.toString()).concat(selectedText.toString()).concat(end.toString()), (error, stdout, stderr) => {
                if (error) {
                    vscode.window.showWarningMessage(error.message);
                }
                else if (stderr) {
                    vscode.window.showWarningMessage(stderr);
                }
                else {
                    editor.edit(editBuilder => {
                        editBuilder.insert(editor.selection.anchor, stdout); // put text at active location in script
                    });
                }
            });
        }
    });
    context.subscriptions.push(disposable);
    let dateTime = new Date().toLocaleString();
    let disposable2 = vscode.commands.registerCommand('llm-assistant.giveTime', () => {
        vscode.window.showInformationMessage(dateTime);
    });
    context.subscriptions.push(disposable2);
    let disposable3 = vscode.commands.registerCommand('llm-assistant.viewTitle', () => {
        vscode.window.showInformationMessage("viewTitle!");
    });
    context.subscriptions.push(disposable3);
}
exports.activate = activate;
// This method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map