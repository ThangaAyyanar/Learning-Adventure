# Vim 100 day challege

I try to learn vim every day and post what i learn everyday 

## Simple TODO:

- [x] Package Manager
- [x] File Browser - nerd tree
- [ ] Motions
- [ ] Fuzzy search
- [ ] Auto pair brackets
- [x] Awesome status bar
- [x] Theme
- [ ] Tmux integration
- [ ] Bulk comment source code
- [ ] Autocompletion and Language Server Protocol
- [ ] File Specific Settings
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

# Reference
* Package Installer: [https://github.com/junegunn/vim-plug](https://github.com/junegunn/vim-plug)
* Plugins: [https://vimawesome.com/](https://vimawesome.com/)

# Youtube Videos
* [NeoVim + LSP setup from scratch](https://www.youtube.com/watch?v=ZrySdB6pUCA)
