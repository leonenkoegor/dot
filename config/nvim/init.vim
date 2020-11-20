call plug#begin('~/.config/nvim/plugged')
Plug 'mhinz/vim-startify'
Plug 'vim-airline/vim-airline'
Plug 'kien/rainbow_parentheses.vim'
Plug 'ObserverOfTime/coloresque.vim'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'junegunn/fzf'
Plug 'spolu/dwm.vim'
call plug#end()

set rnu
set nu
let mapleader=" "

nnoremap <Leader>ff :FZF<CR>
nnoremap <Leader>ve :e $MYVIMRC<CR>
nnoremap <Leader>vr :source $MYVIMRC<CR>

au VimEnter * RainbowParenthesesToggleAll
