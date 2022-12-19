# Emacs 100 day challenge

## Day 1 
### Occur Mode
- Matched regex strings are shown in different buffer called *occur* buffer.

### Prettify Json
- Select the text you want to pretify (I use evil-mode so it is capital v for me)
- Then M-x json-pretty-print
- We can also pretify the current buffer, using `json-pretty-print-buffer`

### Global key mapping example
```
(global-set-key (kbd "M-o") `consult-buffer)
```
refer: https://www.masteringemacs.org/article/mastering-key-bindings-emacs
