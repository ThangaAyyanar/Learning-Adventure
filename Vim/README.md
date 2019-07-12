# Vim 100 day challege

I try to learn vim every day and post what i learn everyday 

## Simple TODO:

- [x] Package Manager
- [x] File Browser - nerd tree
- [ ] Motions
- [x] Fuzzy search
- [ ] Auto pair brackets
- [x] Awesome status bar
- [x] Theme
- [ ] Tmux integration
- [x] Bulk comment source code
- [ ] Autocompletion and Language Server Protocol
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


# Reference
* Package Installer: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
* Plugins: [https://vimawesome.com/](https://vimawesome.com/)

# Youtube Videos
* [NeoVim + LSP setup from scratch](https://www.youtube.com/watch?v=ZrySdB6pUCA)
