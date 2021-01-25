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
- [X] Goyo integration
- [x] multiple cursor
- [x] Autocompletion and Language Server Protocol
* - [x] Swift
* - [x] Rust

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

## Day 23 - Goyo Integration

Plug package
```
Plug 'junegunn/goyo.vim'
```

enter and exit from goyo using the following command
```
:Goyo
```

goyo configuration (lot of plugins are disabled inside goyo to enable it we use the following)
```
function! s:goyo_enter()
    colorscheme molokai
endfunction

"function! s:goyo_leave()
    "colorscheme molokai
"endfunction

autocmd! User GoyoEnter nested call <SID>goyo_enter()
"autocmd! User GoyoLeave nested call <SID>goyo_leave()

```

## Day 24 - Buffers,Tweaking and fugitive

source: https://hashrocket.com/blog/posts/understanding-the-buffer-list-in-vim-part-1

```
:ls - list all the buffers
:bnext - move to next buffer
:bprev - move to previous buffer
:badd - add new buffer
:bdelete - delete buffer
:buffer <TAB> - navigate to the buffer
:only - view the buffer in full page

:sbfirst - open first buffer in new window
```

start vim without plugins
```
vim -u NONE fileyouwantopen
```

check the startup time and debug in neo vim
```
nvim --startuptime <Filename_to_save_output>
```

learned few things about fugitive
```
https://gist.github.com/mikaelz/38600d22b716b39b031165cd6d201a67
```

## Day 25: Multiple cursor

Installed 
```
vim-multiple-cursors 
```
ctrl+n is the command used to edit multiple line 
This plugin is awesome.

## Day  26: Sessions && spell check

spell checking in vim
```
set spell
```
create session
```
:mksession <SessionName>.vim

#open it using
vim -S <SessionName>.vim
```
Tab shortcuts
```
gt,gT
```

## Day 27: Removed deoplete and Installed COC as completion engine

- Coc is **Awesome**

issue faced
```
python jedi completion engine not worked properly so i disabled it 
```
I used **Microsoft Python Language Server** for python Language server

Coc configuration
```
{
    "python.jediEnabled": false,
    "python.pipenvPath":"/usr/local/bin/pipenv"
}

```

Added Status details in lightLine.vim
```
let g:lightline = {
      \ 'colorscheme': 'one',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'cocstatus', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'fugitive#head',
      \   'cocstatus': 'coc#status'
      \ },
      \ }

```

also installed

Vim,Json,Swift(in progress),flutter

Change FZF settings
```
if executable('fzf')
    nnoremap <c-p> :FzfGFiles<cr>
    let g:fzf_command_prefix = 'Fzf'
endif
```

## Day 28 - Finally found the trick to search the yanked text

Run macro across multiple lines

In Normal Mode:  <num of lines>@<macro name>
In Command Mode: :<num of lines> norm @<macro name>
```
"ayy - Read current line into register 'a'
"Ayy - Append the current line to register 'a' (Using capitals for register will no over write but append to the regsiter)
"bP - Paste contents of register 'b' above current line
"cc3w - Change three words, putting the previous three words into register 'c'
````
q: - opens a new split window with the last run vim column commands

/Ctrl - r + 0: search for the yanked text

* - search current word within the file.
\# - search backward.
g* - search part of the current word
g# - search backwards

search can also be combined with operator commands :)

for e.g: y/function - will yank everything from the current position uptil the function text

d?; - will delete everything from current position to the previous occurence of ;

v/test - will select everything from the current position to the next occurence of test.

c2/end - change all the text from the current cursor position upto the second occurence of end word.

<Ctrl-a> if your cursor is over a number it increments that number
<Ctrl-x> if your cursor is over a number it decrements that number
    
**From Primeagen**
f<character> to move forward
```
; -> next
, -> prev
```
    
 mark across the file using 
 ```
 m+<CaptialLetter>
 ```

## Day 29 - multiple file select in FZF

from : https://github.com/junegunn/fzf.vim/issues/40

It's already possible:
```
    tab - select and move cursor down
    shift-tab - select and move cursor up (for some reason, neovim doesn't support the key)
    ctrl-a alt-a - select all
    ctrl-d alt-d - deselect all
    enter / ctrl-x / ctrl-v / ctrl-t - open selected entries (current window / horizontal splits / vertical splits / tabs)
```
Selected entries are added to quickfix list.

## Day 30 - Global commands

Hover definition in COC
```
SHIFT+K -> hover defn
```
Easy navigation in the buffer using plugins: Easy motion or sneak ( on list need to install one )

we can specify range infront of commands
```
.,$left -> remove whitespace infront of sentance from current line to the end
.,.+5left -> remove from current line to current line + 5
```

global command
```
:g/pattern/command
:g/^/pu=\"\n\" -> new line after every line
:g/^\s*$/d -> delete all empty line
:g/pattern/t$ -> copy text with pattern and paste it at end of the line
```

## Day 31 - Copy selected text

This function will copy the matches and store it in given registers
this code is taken from: https://vim.fandom.com/wiki/Copy_search_matches
```
function! CopyMatches(reg)
  let hits = []
  %s//\=len(add(hits, submatch(0))) ? submatch(0) : ''/gne
  let reg = empty(a:reg) ? '+' : a:reg
  execute 'let @'.reg.' = join(hits, "\n") . "\n"'
endfunction
command! -register CopyMatches call CopyMatches(<q-reg>)
```

## Day 32 - VimiWiki & Tabular

making markdown as default style for vim wiki

```
" Vim wiki
let g:vimwiki_list = [{'path': '<DIR>','syntax': 'markdown','ext': '.md'}]
let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
```

Tabular plugin - cucumbertables (tim pope code)
automatically resize table when using '|' as table seperator 

```
"{{{Tabular plugin tricks

inoremap <silent> <Bar>   <Bar><Esc>:call <SID>align()<CR>a

function! s:align()
  let p = '^\s*|\s.*\s|\s*$'
  if exists(':Tabularize') && getline('.') =~# '^\s*|' && (getline(line('.')-1) =~# p || getline(line('.')+1) =~# p)
    let column = strlen(substitute(getline('.')[0:col('.')],'[^|]','','g'))
    let position = strlen(matchstr(getline('.')[0:col('.')],'.*|\s*\zs.*'))
    Tabularize/|/l1
    normal! 0
    call search(repeat('[^|]*|',column).'\s\{-\}'.repeat('.',position),'ce',line('.'))
  endif
endfunction
"}}}
```

json formatter inside neovim using jq

```
nnoremap <leader>j V:!jq<cr>:set filetype=json<cr>
```

## Day 33 - Emoji plugin

customizing gitguter using vim emoji plugin

Plug 'junegunn/vim-emoji'

```
" git gutter setups
let g:gitgutter_sign_added = emoji#for('small_blue_diamond')
let g:gitgutter_sign_modified = emoji#for('small_orange_diamond')
let g:gitgutter_sign_removed = emoji#for('small_red_triangle')
let g:gitgutter_sign_modified_removed = emoji#for('collision')
```

## Day 34 - Time travel

Time travel

Vim can also travel to a state in the "past" and "future". The :earlier and :later commands accept time as an argument:
```
:earlier 5s     " go to older state 5 seconds before
:earlier 5m     " go to older state 5 minutes before
:earlier 5h     " go to older state 5 hours before
:earlier 5d     " go to older state 5 days before
:earlier 5f     " 5 saves ago
```
You can use same argument on :later:
```
:later 5s     " go to newer state 5 seconds after
:later 5m     " go to newer state 5 minutes after
:later 5h     " go to newer state 5 hours after
:later 5d     " go to newer state 5 days after
:later 3f     " 3 saves later
```
site: https://dev.to/iggredible/learn-how-to-use-vim-undo-to-time-travel-3l73

## Day 35 - FZF customization

user Rg to search for strings in file
added custom keyboard shortcuts for files,rg,buffers,gitFiles and changed layout of fzf

```
if executable('fzf')
    let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline'
    let $FZF_DEFAULT_COMMAND="rg --files --hidden" 
    nnoremap <c-p> :FzfFiles<cr>
    nnoremap <c-f> :FzfRg<cr>
    nnoremap <leader>b :FzfBuffers<cr>
    nnoremap <leader>g :FzfGitFiles<cr>
    " All commands provided by fzf will have this prefix
    let g:fzf_command_prefix = 'Fzf'
    " Border color
    let g:fzf_layout = {'up':'~90%', 'window': { 'width': 0.8, 'height': 0.8,'yoffset':0.5,'xoffset': 0.5, 'highlight': 'Todo', 'border': 'sharp' } }
endif

```
refered from **chrisatmachine**

## Day 36 - Fugitive

Learning new things in git fugitive

* git add . | add all unstaged files
* Gstatus   | show git index files (press '-' to stage and unstage files)
  Shift+c   | in gstatus will commit the files directly
* Gdiff     | diff the changes you have done with old version of file
* Gedit :0  | current version of the file from old version

learned from https://github.com/tpope/vim-fugitive

## Day 37 - Unimpaired & status bar update
Installed unimpaired plugin
Few shortcuts is provided in unimpaird plugin such as navigate through buffers,quickfix..

```
function! LightlineGitGutter()
  if !get(g:, 'gitgutter_enabled', 0) || empty(FugitiveHead())
    return ''
  endif
  let [ l:added, l:modified, l:removed ] = GitGutterGetHunkSummary()
  return printf('+%d ~%d -%d', l:added, l:modified, l:removed)
endfunction

let g:lightline = {
      \ 'colorscheme': 'one',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'githunk','gitbranch', 'cocstatus', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'githunk': 'LightlineGitGutter',
      \   'gitbranch': 'fugitive#head',
      \   'cocstatus': 'coc#status'
      \ },
      \ }
```
Added git gutter details to the status
reference: https://gitlab.com/polyzen/dotfiles/blob/dce37955a745ee23efd247306781f8bc4a4d62bc/base/.vim/vimrc#L158

## Day 38

Create my own function TodoTaskWarrior
 - Used to mark line in a file for todo which will straight to task warrior. 
 - function also annotate the task with absolute filename with line number.
```
function TodoTaskAdd()
    "https://coderwall.com/p/auy6fa/vim-get-current-file-path
    let annotation = expand('%:p')
    let task = expand("%:t")
    let lineNumber = line(".")
    execute '!task rc.data.location=~/TaskBase/Office add '.task.' +Todo project:Remainder'
    execute '!task rc.data.location=~/TaskBase/Office +LATEST annotate "file:'.annotation.':'.lineNumber.'"'
endfunction
```
## Day 39 Installed Vim Zettel

Zettel AKA slip box, is a note taking method this plugin provides this feature on top of vimwiki,
tried out yesterday which is pretty cool 

Issue i faced are there is no video tutorial or gif explaining how this plugin work so i read below two
reference multiple times to get that i need
```
Plug 'michal-h21/vim-zettel', { 'for': 'markdown' }
```
configuration setting
```
let g:zettel_format = '%Y%m%d%H%M-%S'
let g:zettel_options = [{},{"front_matter" : {"tags" : ""}, "template" :  "~/Templates/zettel.tpl"}]
let g:zettel_fzf_command = "rg --column --line-number --ignore-case --no-heading --color=always "
nnoremap <leader>vt :VimwikiSearchTags<space>
nnoremap <leader>vs :VimwikiSearch<space>
nnoremap <leader>gt :VimwikiRebuildTags!<cr>:ZettelGenerateTags<cr><c-l>
nnoremap <leader>zl :ZettelSearch<cr>
nnoremap <leader>zn :ZettelNew<cr><cr>:4d<cr>:w<cr>ggA
nnoremap <leader>bl :VimwikiBacklinks<cr>
```
let g:vimwiki_list = [{'path': '~/Documents/My Library','syntax': 'markdown','ext': '.md'},{"path":"~/SlipBox", 'auto_tags': 1, 'auto_toc': 1,'syntax': 'markdown','ext': '.md'}]

let g:zettel_options = [{},{"front_matter" : {"tags" : ""}, "template" :  "~/Templates/zettel.tpl"}]

it has empty dict as first element because i use slipbox method on second wiki element and
another thing that drive me nuts is we need to create index.md or index.wiki file in the Wiki List path otherwise
Zettel commands doesnot appear. so keep that in mind.

nnoremap <leader>gt :VimwikiRebuildTags!<cr>:ZettelGenerateTags<cr><c-l> (command is taken from reddit post)
    
i changed VimiWikiGenerateTags to ZettelGenerateTags, which works best 

reference:
https://www.reddit.com/r/Zettelkasten/comments/fidaum/vimzettel_an_addon_for_the_vimwiki_addon_for_vim/
https://github.com/michal-h21/vim-zettel

## Day 40 - CSS color plugin and LightLine (status bar) changes

Css color - **Plug 'ap/vim-css-color'** highlight hex colors
window zoom - ***Plug 'dhruvasagar/vim-zoom'** zoom window,similar to tmux pane zoom

light line inacitve theme color change
```
autocmd VimEnter * call SetupLightlineColors()
function SetupLightlineColors() abort
  let l:palette = lightline#palette()
  let l:palette.inactive.left = [["#282c34","#ff8c66",235,168,"bold"],["#abb2bf","#3e4452",145,240]]
  call lightline#colorscheme()
endfunction
```
Light line mode changes
```
let g:lightline = {
      \ 'mode_map': {
      \ 'n' : 'N',
      \ 'i' : 'I',
      \ 'R' : 'R',
      \ 'v' : 'V',
      \ 'V' : 'VL',
      \ "\<C-v>": 'VB',
      \ 'c' : 'C',
      \ 's' : 'S',
      \ 'S' : 'SL',
      \ "\<C-s>": 'SB',
      \ 't': 'T',
      \ },
      \ 'colorscheme': 'one',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'githunk','gitbranch', 'cocstatus', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'githunk': 'LightlineGitGutter',
      \   'gitbranch': 'fugitive#head',
      \   'cocstatus': 'coc#status'
      \ },
      \ }
```

## Day 41 - changed few key bindings

```
nnoremap <space><space> :FzfBLines<cr>
nnoremap <leader>b<space> :FzfBuffers<cr>
```

changed color for inactive mode in lightline
```
autocmd VimEnter * call SetupLightlineColors()
function SetupLightlineColors() abort
  let l:palette = lightline#palette()
  let l:palette.inactive.left = [["#282c34","#ff8c66",235,168,"bold"],["#abb2bf","#3e4452",145,240]]
  call lightline#colorscheme()
endfunction
```

## Day 42 - Folding
Need to get started to use folding
so enabled folding
```
set foldmethod=indent
```
we can enable fold column which show few details about folding level
```
set foldcolumn=1
```
Easy to navigate between source file using the following commands
```
zj - next fold
zk - prev fold
zM - fold everything
zR - unfold everything
```
color for folded text
```
highlight Folded guifg=PeachPuff4
highlight FoldColumn guibg=darkgrey guifg=white
```

## Day 43 

We include many times we want 
```
d<count>i{ 
```
stole it from Primeagen video

## Day 44 
File and window related tricks
```
ctrl + ^   to swap between files
:resize constant - resize the window
:vertical resize constant - resize the window
```

Vim trick to bring file directory list (similar to nerd tree)
```
nnoremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
```

## Day 45

View your history from command mode
```
    : to enter command mode
    ctrl-f to open the command history
    k to arrow up and select a previous command
    Enter to run the command
    : to enter command mode again
    ctrl-f to open the command history
    ctrl-c to close the command history
    Esc to exit command mode
```
from **Colin Bartlett** weekly email letter

## Day 46
Write with sudo without leaving Vim
```
:w !sudo tee %
```
Handy Plugins to do this thing in simple manner
```
eunuch.vim plugin
you’ll have an easy option with the handy :SudoWrite command.
```
from **Colin Bartlett** weekly email letter

## Day 47 ( g - Goodness )
```
g + ctrl-g   get more details about current offset, percentage
g8           ascii code of a character
g<           open the console ouput once again
gf           goto file path which is currently present under cursor
g&           replace last subsitute command globally in the file
J            Move the below line text to current line with space
gJ            Move the below line text to current line with identation
gq           indent line to columnwidth(80) per row
gQ           go to EX-mode (:visual mode to get back)
8g_          jump 8 line below and put the cursor at end of the line
g??          rot13 on the line
gv           Rehighlight the last highlighted text
gi           jump to last insert mode cursor location
```
## Day 48 

Live subtitution in neovim
```
set inccommand=nosplit
```

## Day 49 - xml beautify inside vim

```
:'<,'>!xmllint --format -
```
reference: https://stackoverflow.com/questions/21408222/vim-indent-xml-file

## Day 50 - fugitive 2

Git mapping for Resolving conflicts
```
nnoremap <leader>gg :diffget<cr>
nnoremap <leader>gf :diffget //2<cr>
nnoremap <leader>gh :diffput //3<cr>
nnoremap <leader>gs :G<cr>
" dv - on :G to resolve
```

FZF integration for git checkout using **Plug 'stsewd/fzf-checkout.vim'**
```
    "FZF git checkout plugin
    let g:fzf_checkout_create_key = 'ctrl-c'
    nnoremap <leader>gc :FzfGCheckout<cr>
```
Reference: https://www.youtube.com/watch?v=PO6DxfGPQvw    
           https://www.youtube.com/watch?v=73RulF4Md4Q

## Day 51 - Trying Fern.vim
Async file manager 
```
Plug 'lambdalisue/fern.vim'
Plug 'lambdalisue/nerdfont.vim'
Plug 'lambdalisue/glyph-palette.vim'
Plug 'lambdalisue/fern-renderer-nerdfont.vim'
```
to support nerd font
```
let g:fern#renderer = "nerdfont"
```

## Day 52 - COC Search 
The CocSearch can search contents in entire project.
Anything edited in search window will save to the file,
- We can replace variable in entire project
- We can also execute macros

Search the word on the cursor (Mapping)
```
nnoremap <leader>cs :CocSearch <C-R>=expand("<cword>")<CR><CR>
```

We can also provide **rg** options to coc search as it uses at it backend
eg:
Bring 20 lines after the matched text
```
:CocSearch <text/regex> -A 20
```

Reference: (The Primeagen video) https://www.youtube.com/watch?v=q7gr6s8skt0

## Day 53 - Search and replace (zs,ze)

As a quick example, say you have a line like 
```
test testing tester
```
:s/test/foo/g        gives **foo fooing fooer**    
:s/\zstest\zeing/foo gives **test fooing tester**

## Day 54 - sort command

Sort lines in Vim:

* :sort - sort all lines
* :sort! - sort in reverse
* :sort u - removes dupes and sort
* :sort i - ignore case
* :sort n - sort numerically

From: @vim_tricks (twitter account)

## Day 55 - Terminal configuration

Terminal -> Normal remap
```
"terminal remap
tnoremap <C-[> <C-\><C-n>
```
Terminal auto configuration when entered and closed from terminal
```
" Terminal Enter and close
function Terminal_enter()
    set relativenumber!
    set number!
    set signcolumn=no
    startinsert
endfunction

function Terminal_close()
    set relativenumber
    set number
    set signcolumn=yes
endfunction

autocmd TermOpen * :call Terminal_enter()
autocmd TermClose * :call Terminal_close()
```
Navigation from terminal to windows
```
tnoremap <c-h> <C-\><C-N><C-w>h
tnoremap <c-j> <C-\><C-N><C-w>j
tnoremap <c-k> <C-\><C-N><C-w>k
tnoremap <c-l> <C-\><C-N><C-w>l
```
## Day 56 - hightlight matching words like vscode and intellj

```
Plug 'RRethy/vim-illuminate'
```

## Day 57 - Run Neovim nightly and stable in same machine

**ASDF** is a program that can handle the version management.    
reference: https://github.com/asdf-vm/asdf

#### Step i followed
* Removed the default neovim
* Install asdf (check the above link)
* Add neovim plugin
```
asdf plugin-add neovim
```
* Install neovim version - stable and set stable version as default.
```
asdf install neovim stable
asdf global neovim stable
```
* Install neovim version - nightly 
```
asdf install neovim nightly
```
* Enable nightly when you need it (using shell command)
```
asdf shell neovim nightly
```
## Day 58 - Open Vim to a specific line

    vim myfile.js +10 - Opens myfile.js, jumps to line 10

    vim +10 myfile.js - Same! Argument order doesn’t matter
    
 source: Colin Bartlett (Newsletter)
 
 plugins similar to this   
 https://github.com/wsdjeg/vim-fetch
 ```
vim path/to/file.ext:12:3 in the shell to open file.ext on line 12 at column 3
:e[dit] path/to/file.ext:100:12 in Vim to edit file.ext on line 100 at column 12
gF with the cursor at ^ on path/to^/file.ext:98,8 to edit file.ext on line 98, column 8
gF with the selection |...| on |path to/file.ext|:5:2 to edit file.ext on line 5, column 2
 ```

## Day 59 - Global command example

Quickly remove all empty lines
```
:g/^$/d
```

## Day 60 - Rest api from vim
- We need to have curl installed to do this trick
```
nnoremap <leader>cc vipyPgvO<Esc>O<Esc>gv:!curl --config -<CR>
```
resources: 
- https://nazarii.bardiuk.com/posts/vim-curl.html

Plugin which does things bit better
- https://github.com/diepm/vim-rest-console

## Day 60 - Vim args (multiple file search and replace)

open the relevant files to do changes
```
:args <Files>
or
:args <Glob>

eg:
args path/*
```
Subtitution
```
argodo %s/find/replace/g
```
save the changes
```
argdo update
```
Learned from: @vim_tricks (twitter)

## Day 61 - Scroll bind
Have you ever faced a suitation where you open two files and need to scroll them simultaneously, This can be acheived using
```
set scrollbind
```
Learned from: @vim_tricks (twitter)

## Day 62 - Quickfix

previous Quickfix list
```
:colder
```
next Quickfix list
```
:cnewer
```
Learned from: @vim_tricks (twitter)

## Day 63 - search through the keybinding

search through the keybindings
```
:filter pattern imap <insert mapping>
:filter pattern nmap <normal>
```
Learned from: @vim_tricks (twitter)

## Day 64 - execute one normal command from insert mode 

```
ctrl+o 

then execute one normal keymap and it will be automatically go back to insert mode
```
Learned from: https://appletree.or.kr/quick_reference_cards/Unix-Linux/vim-modes-transition-diagram.svg

## Day 65: UML diagram in Vim

- https://github.com/skanehira/preview-uml.vim
- interactive uml diagram generation using the above plugin.
- It uses plant uml to acheive it

## Day 66: Vim multi cursor changed

```
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
```
as the previous used plugin got deprecated

## Day 67: Smooth scrolling & hoon syntax highlight

```
Plug 'psliwka/vim-smoothie'
Plug 'urbit/hoon.vim'
```

# Day 68: Git fugitvie

Git history of a folder or file
```
Glog -- %
```
Git log taking long time
```
Glog -<number> = limit
Glog -100 for swift responses
```
source: ThePrimeagen Twitter feed

## Day 69: Snippets

The snippets collection plugin
```
Plug 'honza/vim-snippets'
```
snippets completion is taken care of **coc**
```
:cocinstall coc-snippets
```
source: https://www.chrisatmachine.com/Neovim/17-snippets/

## Day 70: Python Playground and Jupyter like environment
```
Plug 'jupyter-vim/jupyter-vim'
```
For jupyter vim need to attach to **qtconsole** ( the reason for using qtconsole to display images, plots )

```
Plug 'metakirby5/codi.vim'
```

to start codi which is similar to playground in xcode, display the instant result near the command
```
:codi
```

sources:
- https://github.com/broesler/jupyter-vim#info
- https://github.com/metakirby5/codi.vim

## Day 71: Mobile developement using Flutter

- It works out of the box using **coc-flutter** but come across few issues such as Hotreload is not working
- vWorkaround i spawn terminal in vim and run it.

- Developed a sample app, encounters lot of alignment related issues.

## Day 72: ctrl+y and ctrl+e

ctrl+y and ctrl+e two binding in the insert mode, insert character above and below the current line

Learned from: @vim_tricks (twitter)

## Day 73: Append selected text to file

Use >> before your filename to append rather than overwrite.
```
:w >>path/to/new/file.rb<Enter> appends the lines to the existing file
```

## Day 73: ctrl+g and ctrl+t from search bar

you can able to move to next and previous word matches current searches from search bar without pressing enter

Learned from: @vim_tricks (twitter)

## Day 74: Scrolloff

```
set scrolloff=<num>
```
able to scroll before <num> from bottom

Learned from primeagen video

## Day 75: Override vim runtime 

```
 -u vimrc

Use vimrc instead of the default ~/.config/nvim/init.vim.  If vimrc is NORC, do not load any initialization files (except plugins), and do not attempt to parse environment variables.  If vimrc is NONE, loading plugins is also skipped.

:help initialization
```

# Books
* [Learn vim the hard way](http://learnvimscriptthehardway.stevelosh.com/)
* [Learn Vim (the Smart Way)](https://github.com/iggredible/Learn-Vim) recommends for begineers (Work In Progress)

# Awesome blog articles
* https://www.brianstorti.com/vim-registers/
* https://stackoverflow.com/questions/3031009/what-does-the-compiler-command-do-in-vim ( How to use compiler folder in vim runtime )
* https://castel.dev/ ( Lecture notes using Vim+Latex+Inkscape )

# Awesome Plugins (Need to check)
- [ ] https://github.com/mhinz/neovim-remote

# Reference
* Package Installer: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
* Plugins: [https://vimawesome.com/](https://vimawesome.com/)
* Blog: [Chris at machine](http://chrisatmachine.com)

# Youtube Videos
* [NeoVim + LSP setup from scratch](https://www.youtube.com/watch?v=ZrySdB6pUCA)
* [Talk on going mouseless with Vim, Tmux, and Hotkeys](https://www.youtube.com/watch?v=E-ZbrtoSuzw)
* [vim + tmux - OMG!Code](https://www.youtube.com/watch?v=5r6yzFEXajQ)
* [Let vim do the typing](https://www.youtube.com/watch?v=3TX3kV3TICU)

# Other vimrc's
* https://github.com/mattboehm/dotfiles/blob/master/vim/vimrc
* https://raw.githubusercontent.com/tojochacko/vim/master/commands-list

