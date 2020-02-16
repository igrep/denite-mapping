# denite-mapping

denite.nvim source for key mappings. (Partial) port of the mapping source of unite.vim.  
I used to use the feature in unite.vim only for searching.  
So I ported only the searching feature: the denite-mappoing source provides no actions so far.

In the future, I might add a feature to open the line where the mapping is defined.  
It would be implemented with `:verbose map` command and the `line` kind of denite.nvim.
