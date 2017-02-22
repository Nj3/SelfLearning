set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Bundle 'Valloric/YouCompleteMe'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'kien/ctrlp.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set nu

set clipboard=unnamed

au BufNewFile,BufRead *.py
    \ set tabstop=4|
    \ set softtabstop=4|
    \ set shiftwidth=4|
    \ set textwidth=79|
    \ set expandtab|
    \ set autoindent|
    \ set fileformat=unix

au BufRead,BufNewFile *.py match BadWhitespace /\s\+$/

set encoding=utf-8

let g:ycm_autoclose_preview_window_after_completion=1

let python_highlight_all=1
syntax on

if has('gui_running')
          set background=dark
            colorscheme solarized
    else
              colorscheme zenburn
      endif

call togglebg#map("<F5>")

let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

let g:ycm_server_python_interpreter = '/usr/bin/python3'
let g:ycm_python_binary_path = '/usr/bin/python3'

"run
autocmd FileType python nnoremap <buffer> <F9> :exec '!python3' shellescape(@%, 1)<cr>
"save
:map <F2> :w <Enter>
