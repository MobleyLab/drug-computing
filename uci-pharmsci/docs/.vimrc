set nocompatible
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set ignorecase smartcase
set incsearch
set pastetoggle=<F2>
syntax enable

"set foldmethod=indent
"set foldnestmax=1

" Make 80th column in python code be magenta
highlight ColorColumn ctermbg=magenta
au FileType python,sh,slurm,tcl,namd,inp call matchadd('ColorColumn', '\%80v', 100)

" Strip trailing whitespace from lines in programs
autocmd FileType c,cpp,java,php,python autocmd BufWritePre <buffer> %s/\s\+$//e

" Always show statusline
set laststatus=2

" Use 256 colours (Use this setting only if your terminal supports 256 colours)
set t_Co=256
