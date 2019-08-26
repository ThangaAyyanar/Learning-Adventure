# Vim 100 day challege

I try to learn vim every day and post what i learn everyday 

## Simple TODO:

- [x] Package Manager
- [x] File Browser - nerd tree
- [x] Tagbar
- [x] Fuzzy search
- [x] Auto pair brackets
- [x] Awesome status bar
- [x] Theme
- [x] Tmux integration
- [x] Bulk comment source code
- [ ] Autocompletion and Language Server Protocol
* - [ ] Swift
* - [x] Rust
- [ ] File Specific Settings (ftplugin )
* - [ ] Swift
* - [ ] Rust
* - [ ] Dart

## Day 1

Installed Package Manager  

```
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

set leader key

```
let mapleader = ","
```

File Browser

```
Plug 'scrooloose/nerdtree'

nnoremap <leader>a :NERDTreeToggle<CR>
```

Theme
```
Plug 'tomasr/molokai'

let g:molokai_original = 1
colorscheme molokai
```

Status Bar
```
Plug 'bling/vim-airline'
```

Basic Things
```
" to quit
nnoremap <leader>q :q!<CR>

" to clear matched searches
nnoremap <leader><space> :nohlsearch<CR>

" create new splits easily
map <leader>h :<C-u>split<CR>
map <leader>v :<C-u>vsplit<CR>

" ESC mapping to jj
inoremap jj <ESC>

" set cursor line (to highlight current line),line number, highlight search
set cursorline
set number
set hlsearch
```
#### Map and remap

remap is an option that makes mappings work recursively. By default it is on and I'd recommend you leave it that way. The rest are mapping commands, described below:

:map and :noremap are recursive and non-recursive versions of the various mapping commands. What that means is that if you do:
```
:map j gg
:map Q j
:noremap W j
```
j will be mapped to gg. Q will also be mapped to gg, because j will be expanded for the recursive mapping. W will be mapped to j (and not to gg) because j will not be expanded for the non-recursive mapping.

source: https://stackoverflow.com/questions/3776117/what-is-the-difference-between-the-remap-noremap-nnoremap-and-vnoremap-mapping

## Day 2

enable mouse support and not interfere with tmux scroll 
```
set mouse=a
```
syntax highlighting for swift
```
Plug 'keith/swift.vim'
```
In vim when you close the undo operation is earsed which is pretty annonying
retain value after terminating file
```
set undofile
set undodir=/tmp
```
want to check what are all the options in the set variable type
```
set variable?

example:

set number?
```
Clipboard sharing - checked in mac
```
set clipboard=unnamed
```
Better verical movement - particullary in long sentence in line 
```
nnoremap j gj
nnoremap k gk
```

Move between split easily
```
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l
```

relative number toogle
```
" set variable can be toggled by adding ! at the end
nnoremap <leader>n :<C-u>set relativenumber!<CR>
```

## Day 3

Plugins
```
" show file changes near the line number
Plug 'airblade/vim-gitgutter'

" grep the data
Plug 'mileszs/ack.vim'

" Fuzzy finder
Plug 'junegunn/fzf'

" rust syntax highlighting 
" below command will load it when we open the rust file
Plug 'rust-lang/rust.vim', {'for': 'rust' }
```

learned few nerdTree options which can open the file from it and expand and close the file tree.
learned about vim folding 

Display hidden characters tab and End of Line
```
set list
set listchars=tab:▸\ ,eol:¬
```

Tab options which makes formatting pretty
```
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set smarttab
```
ack plugin options configuring ripgrep
```
if executable('rg')
    let g:ackprg='/usr/local/bin/rg --vimgrep'
    nnoremap <leader>r :Ack!
endif
```

Fuzzy finder mapping with vim
```
if executable('fzf')
    nnoremap <C-p> :FZF<cr>
endif
```
Quickly insert a timestamp 
```
nnoremap tt "=strftime("%F %T%z")<CR>p
```

## Day 4

changed the time stamp format
```
nnoremap tt "=strftime("%d %b %Y %X")<CR>p
```
Git Gutter sign column
```
set signcolumn=yes
```

column limit
```
set textwidth=80
set colorcolumn=80
```

Git command integrations
```
" git basic commands
Plug 'tpope/vim-fugitive'

" git shows the selected line in the browser
Plug 'tpope/vim-rhubarb'
```

## Day 5

Language Server Protocol configuration and Autocompletion

**LSP reference:**
* https://langserver.org/
* https://microsoft.github.io/language-server-protocol/implementors/tools/

```
" provides the autocompletion feature
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }

" LSP client for vim
Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }
```

deoplete configuration
```
let g:deoplete#enable_at_startup = 1
```

Configuration of rust LSP with Language client neovim and mappings
```
let g:LanguageClient_serverCommands = {
    \ 'rust': ['~/.cargo/bin/rustup', 'run', 'stable', 'rls'],
    \ }

" TODO: Need to change the mappings

nnoremap <leader>c :call LanguageClient_contextMenu()<CR>
" Or map each action separately
nnoremap <silent> K :call LanguageClient#textDocument_hover()<CR>
nnoremap <silent> gd :call LanguageClient#textDocument_definition()<CR>
nnoremap <silent> <F2> :call LanguageClient#textDocument_rename()<CR>
```

There are many ways to open a new buffer with no name, the simplest of which is *:new*.

* *:new* will create a split window with an unnamed buffer.
* *:enew* will open one in the current window.
* *:vnew* will open one in a vertically split window.
* *:tabnew* will open one in a new tab.

source: https://stackoverflow.com/questions/4478111/vim-how-do-you-open-another-no-name-buffer-like-the-one-on-startup

Force syntax coloring
```
:set syntax=php
```

Replace character/String with new line
```
:s/,/,^M/g
```
To get the **^M** character, type *Control-v* and hit *Enter*. Under Windows, do *Control-q, Enter*. The only way I can remember these is by remembering how little sense they make:

## Day 6

Plugins
```
" Highlight yank
Plug 'machakann/vim-highlightedyank'

" Font icons for plugin  
Plug 'ryanoasis/vim-devicons'

" start up screen for vim
Plug 'mhinz/vim-startify'
```

Highlight yank/copied text plugin configuration
```
highlight HighlightedyankRegion cterm=reverse gui=reverse
```
Options for spliting window directions
```
set splitbelow
set splitright
```
use <++> as placeholder for inserting new text - from luke smith vimrc file
```
inoremap <leader><leader> <Esc>/<++><Enter>"_c4l
nnoremap <leader><leader> <Esc>/<++><Enter>"_c4l
```

## Day 7

Get data from help documents
```
:help user-manual
:help index

" search the text in the help documents
:helpgrep <text to search>
" move to next result and prev through the help documents which is found by help grep
:cnext 
:cprev
```

Basic movements

```
i -> insert before the cursor
a -> insert after the cursor

I -> insert at the starting of the sentance
A -> Insert at the end of the sentance

r -> replace the current character
R -> replace the text from the current character

c -> { TODO }
C -> deletes the text after the cursor and spawn the insert mode

s -> subtitute current word (insert mode)
S -> subtitute the whole sentance

H -> move to top of the buffer ( not file)
L -> move to lower end of the buffer ( not file)
M -> move to middle end of the buffer ( not file)
```

Folding
```
" fold based on identation
set foldmehtod=indent

zc -> fold close
zo -> fold open
```
## Day 8

Basic Commands
```
) -> move to next sentance
( -> move to previous sentance
} -> move to next paragraph
{ -> move to previous paragraph

ctrl+o -> jump to previous location
ctrl+i -> jump forward to next location again

~ -> convert uppercase to lowercase and viceversa

ctrl+] -> follow the link in manual ( ctrl+o to come back ).

:cd -> change directory
:earlier 4m -> revert back the file to 4 minute earlier

/ -> to search in normal mode and 'n' to move next occurance & N to previous
occurance
```

Marker: It is helpful to jump back and forth the location in vim
```
ma -> create a mark for letter 'a'
`a -> to jump to that mark
```
we can able to create [a-zA-Z] totally 52 marker for a file

Placeholder which can be later replaced by text
This trick is learned from Luke Smith

```
inoremap <leader><leader> <Esc>/<++><Enter>"_c4l
nnoremap <leader><leader> <Esc>/<++><Enter>"_c4l
```

Diff two different buffer using

```
" this will diff the two buffer
:windo diffthis

" to exit from diff
:windo diffoff
```

Installed tag bar plugin and ctags.

## Day 9

Splits
```
:sp filename 	Open filename in horizontal split
:vsp filename 	Open filename in vertical split

" make the split maximize and minimize using the key bindings
nnoremap <C-W>M <C-W>\| <C-W>_
nnoremap <C-W>m <C-W>=

" Not done in my vim 
```

move splits into tabs
```
:tabedit %
```

Check what are the plugins loaded
```
" where was an option set  
:scriptnames            : list all plugins, _vimrcs loaded (super)  
:verbose set history?   : reveals value of history and where set  
:function               : list functions  
:func SearchCompl       : List particular function
:set runtimepath?       : lists the path of all plugins loaded when a file is opened with Vim.
```

checked about soure kit lsp for swift 

## Day 10 

Just configured few things to make **tagbar**.

auto pair plugin ( automatically close brackets )
```
Plug 'jiangmiao/auto-pairs'
```

## Day 11

In visual mode
select text and press **u** for small letter
or **U** for capital letter
```
c$ : change from current position
<ctrl+w><ctrl+w> : move to next window

:?<word> will search the word backward
    
:!<command> to execute shell commands inside vim

:'<,'>w <Filename> save the selected line as seperated file 
    
:r <filename> to retrieve the filename
    
:r !ls to retrive the command output
```

## Day 12

Plugin installed
```
Plug 'christoomey/vim-tmux-navigator'
```

**Interacting with tmux**

Use these settings in conjuction with `christoomey/vim-tmux-navigator` in .tmux.conf

```
bind -n C-h run "(tmux display-message -p '#{pane_current_command}' | grep -iq vim && tmux send-keys C-h) || tmux select-pane -L"
bind -n C-j run "(tmux display-message -p '#{pane_current_command}' | grep -iq vim && tmux send-keys C-j) || tmux select-pane -D"
bind -n C-k run "(tmux display-message -p '#{pane_current_command}' | grep -iq vim && tmux send-keys C-k) || tmux select-pane -U"
bind -n C-l run "(tmux display-message -p '#{pane_current_command}' | grep -iq vim && tmux send-keys C-l) || tmux select-pane -R"
bind -n C-\ run "(tmux display-message -p '#{pane_current_command}' | grep -iq vim && tmux send-keys 'C-\\') || tmux select-pane -l"
```
## Day 13

Vim magic formula
```
[count][operator][text object/motion]
```
Example:
```
6+ -> 6x go to down to line start
gUaW -> capitalize the word
3ce -> 3x change to word end
4$ -> 4x go to end of life
d]m -> delete to start of next method
% -> jump to match of next paren or bracket
```

Operators
```
c -> change
d -> delete
y -> yank
~ -> swap case
gu -> make lowercase
gU -> make uppercase
< -> shift left
> -> shift right
= -> ident
```

## Day 14

these are taken from 2nd youtube video presentation slides

Text objects (sample)
```
aw -> a word
iw -> inner word
aW -> a WORD
iW -> inner WORD
ap -> a paragraph
ip -> inner paragraph
ab -> a bracket
ib -> inner bracket
at -> a tag block
it -> inner tag block
```

Motions (sample)
```
% -> go first matching paren/bracket
[count] + -> down to first non block char of line
[count] $ -> end of the line
[count] f/F{char} -> to next occurance of char
[count] t/T{char} -> to before next occurance of char
[count] g/h/j/k -> move count direction
[count] ]m  -> go to begining of the method
[count] w/W -> go a word/ WORD to right
[count] b/B -> go a word/ WORD to left
[count] e/E -> go to end of word/ WORD to right
```

## Day 15

print message in the command
```
:echo "Hello world vim"
```
print message in the command and persist
```
:echom "Hello world vim persistant"

" view the message using 
:messages
```

useful when debugging the vim script

## Day 16

Mapping
```
:map <key> <operation>
it will map for all modes

:nmap - normal map
:imap - insert map
:vmap - visual map
```
Example
```
i want to delete whole line in insert mode
:imap <c-d> <esc>ddi

escape from insert mode and delete the line and get back into the insert mode

:imap <c-u> <esc>VUi

this will capitalize the sentence in insert mode ( Exercise in learn vim the hard way )
```

## Day 17

leader keys
```
let mapleader = "-"
" use it like <leader>

:let maplocalleader = "\\"
"use it like <localleader>
```
abbrevation
```
:iabbrev adn and
```

## Day 18

vim auto completion mode using 
**ctrl + x**

then pressing further option can 
able to complete word based on ctags, spell check
or
complete whole sentence

## Day 19

Move through file faster
```
ctrl + u => Up
ctrl + d => down
```

move the editor screen by one line
```
ctrl+e - move down
ctrl+y - move up
```

move through file like pages
```
ctrl + f => forward to next page
ctrl + b => backward to previous page
```

Move to the line number
```
<Number>gg
```

change editor screen showing the current line
```
zt - make line display in top
zb - make line display in bottom
zz - make line display in center
```

inline navigation

```
0 - start of the line
$ - end of the line
^ - start of char
g_ - end of char
```

search the current word in file

```
* - search the current word and move to next occurance
# - search the current word and move to previous occurance
```

## Day 20

autocommands

```
:autocmd BufNewFile * :write
         ^          ^ ^
         |          | |
         |          | The command to run.
         |          |
         |          A "pattern" to filter the event.
         |
         The "event" to watch for.
 
 
 Example::
 -------
 
Vim creates files as soon as you edit them. Run the following command:

:autocmd BufNewFile * :write

:autocmd FileType python     nnoremap <buffer> <localleader>c I#<esc>

```

## Day 21

Operator-Pending Mappings
```
" operator mapping p to i(
:onoremap p i(
```
hello(world)

in above sentance place cursor in world and press 'dp' it will delete all the word inside brackets.

```
:onoremap b /return<cr>
" similar to above but select until return. and do the respective operation (d-delete,c-change,y-yank)
```

## Day 22 - Multiple line editing using two methods

source: https://stackoverflow.com/questions/11784408/vim-multiline-editing-like-in-sublimetext

* visual block
    - press ctrl+v and select the required lines.
    - press 'I' and type text you want.
    - press 'ESC' to affect all the lines.

* global command
```
:g/Hello/d
```
delete line which contains hello

```
:g/Hello/norm dw
```
delete the first word of every line contains hello

# Reference
* Package Installer: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
* Plugins: [https://vimawesome.com/](https://vimawesome.com/)
* Book: [Learn vim the hard way](http://learnvimscriptthehardway.stevelosh.com/)

# Youtube Videos
* [NeoVim + LSP setup from scratch](https://www.youtube.com/watch?v=ZrySdB6pUCA)
* [Talk on going mouseless with Vim, Tmux, and Hotkeys](https://www.youtube.com/watch?v=E-ZbrtoSuzw)
* [vim + tmux - OMG!Code](https://www.youtube.com/watch?v=5r6yzFEXajQ)
* [Let vim do the typing](https://www.youtube.com/watch?v=3TX3kV3TICU)
