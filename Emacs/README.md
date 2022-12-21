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

## Day 2
### Markdown Narrow and Widen
- Used to show only the necessary content in the screen, same is available for org file too.
- `markdown-narrow-*` functions in M-x can narrow down the view.
- `widen` remove the restriction

### Vterm and multi vterm as Termux alternative
- `multi-vterm` to spawn a terminal
- `multi-vterm-rename-buffer` to rename terminal buffer name
- I use it along with `tab` mode.

## Day 3
### Daily diary - one simple function
- Don't know where i found it but i like it.
```
(defun log-diary()
  (interactive)
  (setq filename (concat "~/Documents/Diary/" (format-time-string "%Y-%m-%d") ".md"))
  (find-file filename)
  (insert (concat "# " (format-time-string "%H:%M") "\n\n"))
  (previous-line))

```

## Day 4
### Magit status - change key
- Change `gt` mapping to tab-bar instead of magit function
```
(evil-define-key 'normal magit-status-mode-map (kbd "gt") 'tab-bar-switch-to-next-tab)
```
