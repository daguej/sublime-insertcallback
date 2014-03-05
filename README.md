About
=====

Inserts a node-style JavaScript callback function, and ensures that the call's trailing semicolon is inserted.

Example
=======

Type a function call.  When you type `(`, Sublime will autofill the closing `)`, and your cursor will be between the parens.

    someAsyncFn()

Press <kbd>Alt</kbd>+<kbd>C</kbd>.  If the function call's trailing semicolon is missing, it will be filled in.  A callback function snippet will then be inserted.

    someAsyncFn(function(err, d) {
        
    });

`d` will be selected for changing.  <kbd>Tab</kbd> takes you to the function body.

You can also select existing code and press <kbd>Alt</kbd>+<kbd>C</kbd>; the selected text will be inserted inside the new function body.