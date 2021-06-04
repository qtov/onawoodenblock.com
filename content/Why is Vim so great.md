Title: Why is Vim so important for programmers.
Date: 2021-06-04 17:43
Category: tech
Tags: editor, vim, sublime
Authors: Rexu
Summary: Why do I think vim is the greatest tool for any programmer.

&emsp;So then, why is Vim so goddamn great? And why do a lot of programmers talk about it?
There are a ton of articles as to why Vim is indispensable, but I'm gonna tell it to you simple and easy.

&emsp;I don't use vim, I don't like vim. Vim is hard and it takes too much to make it how I want.
I also use Windows mostly, so I find any vim implementation to have a slow startup and if I want to use the terminal it's sometimes buggy (looking at you cmd).

&emsp;That's why I use is Sublime Text with the NeoVintageous plugin.
I get the rich plugin ecosystem of sublime, with the advantage of vim (in 99% of cases).

How does vim work? Well, vim has a thing called modes.  
When you start the editor you're put in "normal" mode.  
You press `i`/`I`/`a`/`A`/`o`/`O` and you're put in "insert" mode where you... well... insert.  
To leave insert mode, you press `escape`, and you'll be put you back in "normal" mode.  
You press `v`/`V`/`ctrl+v` and you're put in "visual" mode. With visual mode, you select without using your mouse.  
You press `:` to enter command mode.

Imagine you want to select 5 lines `V5j`  
Imagine you want to select upwards without losing what you've already selected `o5k`

&emsp;The main point of vim is... stop using your mouse, it's a pain in the ass to move from keyboard to mouse to keyboard to mouse again and again when everything is so easy to do without the mouse.  
Also, why would you ever want to be in "insert" mode all the time, you lose so many possibilities for movement if you're 24/7 in insert mode.

&emsp;Traditional text editors work like this, they start in "insert" mode and then you have only a limited number of possible movements.  
You can move with the mouse, select with the mouse and drag and drop (not like anyone uses that... right?).  
Then you have the arrow keys, end/home, page up/page down, ctrl+arrow keys (in some editors even alt+arrow keys), and that's all.  
And if you want to select, use those movements while holding shift, which is quite painful from time to time. You can of course, select with mouse. With vim, you just enter insert mode and use all the movement keys like you'd do normally.

&emsp;But what if I told you, that you can use vim in any, or better said in most of the modern editors.  
Most of them will already have a plugin that emulates or even integrates neovim (vim rewritten by other people).

Every key in normal mode does a different thing. For example, if you want to move left down up right you use h j k l. You can also use arrow keys, nobody stops you.  
To enter insert mode, as I said, there are at least 6 keys.

 - `o` inserts a new line below and puts you into insert mode
 - `O` inserts a new line above and puts you into insert mode
 - `i` starts insert mode before the cursor
 - `a` starts insert mode after the cursor
 - `I` stars insert mode at the beginning of the line
 - `A` starts insert mode at the end of the line

&emsp;Vim also makes those keys easy to remember. And once your get over your initial fear of learning vim, you won't be able to live without it, seriously.  
Vim does commands, and those commands are easy to compose.  
To delete one line you use `dd`, what if you want to delete 5 lines? `5dd`  
What if you want to delete 5 lines downwards `5dd` (same as `5dd`, `d4j`).  
What about upwards `d4k`/`4dk` (4 is not a mistake, I'll explain). Those commands translate to:

 - `dd` means delete whole line
 - `<number><command>` (`5dd`) means repeat the command 5 times. Aka, delete 5 lines.
 - `d` is the prefix for a command, that's why when you just press `d` in normal mode, it doesn't do anything until you press another key (or `escape` to cancel). If you press `d` in visual mode when you have already selected something, that will simply delete the selected text.
 - `d4j` now, why 4? Well, when you do `dj` it deletes the current line AND the line below. It literally translates to "delete" this line and the line below (for `d4j` it's this line and the 4 lines below). If you do `4j` it'll move you 4 lines below, exactly where all of those lines would be deleted.

Instead of h j k l you can use arrow keys, but it's easier to have your hands on hjkl.

Now... I lied, `d` doesn't delete, but it's easy to remember it as `d`elete. It actually cuts text, and it puts it in the "unnamed register". Now, I won't talk about registers because the extensions usually use the system clipboard which is the best usecase in my opinion. You can paste in vim with `p` (paste after cursor)/`P` (paste before cursor).

You can move not just letters, but words as well.  
For example:

 - `w` jump to the start of the next word
 - `W` jump to the start of the next word (ignore punctuation)
 - `e` jump to the end of the words
 - `E` jump to the end of the words (ignore punctuation)
 - `b` jump to the beginning of the words
 - `B` jump to the beginning of the words (ignore punctuation)

You can also move by paragraphs `{`/`}`, move to matching paranthesis/brackets `%`.

You can also use `d`elete, `y`ank (copy), `c`hange (same as delete but puts you in insert mode afterwards), using the movement commands. `d5w` (delete 5 words), `d5b` (delete 5 words backwards).

And my favourite thing in vim, `i`n and `a`round.  
Assume you have a `function foo(var_a, var_b, var_c)` and your cursor is on `b` from `var_b`.  
You want to get rid of all parameters and rewrite them `ci(`, which translates to "change in  ()", what if I want to also delete the paranthesis? `ca(` "change around ()".

I have the word `very_long_word_holy_guacamole`, and I my cursor is on `w` from `word`. Without vim I'd do `ctrl+right ctrl+backspace` or `ctrl+right shift+ctrl+left delete/backspace`, with vim I do `ciw` "change in word".  
Every movement command can be used in combination with `d`elete, `y`ank, `c`hange, `v`isual, etc. Every command can be combined with the movement keys.
Now then, all of those were written from memory, it's easy to remember the commands once you use them, and it's a heck of a lot of fun doing so.  
There's also `ctrl+o`/`ctrl+i` to move to last cursor position and back.

My point is, vim is superior to the traditional way of editing text (aka only "insert" mode).

Now, if you want to learn it, there's a good unix command (once you installed vim) called `vimtutor`. It's there in wsl or any unix based operating system, might even be on windows if you install gvim.  
If you don't want to learn it `¯\_(ツ)_/¯`