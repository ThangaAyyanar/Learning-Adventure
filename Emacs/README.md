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
- ~Change `gt` mapping to tab-bar instead of magit function~
- This doesn't worked after i restarted the emacs :(
```
(evil-define-key 'normal magit-status-mode-map (kbd "gt") 'tab-bar-switch-to-next-tab)
```

## Day 5
### Vertico-delete-buffer function
```
(defun vertico-delete-buffer ()
  "Kill buffer in the vertico"
  (interactive)
  ;;(message (and vertico--input (vertico--candidate 'highlight)))
  (kill-buffer (and vertico--input (vertico--candidate 'highlight))))

(with-eval-after-load 'evil
  (define-key vertico-map (kbd "C-d") 'vertico-delete-buffer)
  (define-key vertico-map (kbd "M-h") 'vertico-directory-up))
```
- Hacky way to delete buffer when `c-d` is pressed in `c-x b`
- Getting the hovered content from vertico logic is taken from `consult-vertico--candidate`
- Problems
  - Doesn't work in consult buffer (I don't why)
  - Vertico is updated after the buffer is deleted

### Embark
- Tried embark it works inside the buffer
- Not working in minibuffer, I don't know 
  - I `toggle-debug-on-error` in M-x and ran the embark act on mini buffer, found the following error   
```
Debugger entered--Lisp error: (void-function vertico--update)
  vertico--update()
  embark--vertico-selected()
  #f(compiled-function (fun) #<bytecode -0x4e7c2ce8f1f2874>)(embark--vertico-selected)
  run-hook-wrapped(#f(compiled-function (fun) #<bytecode -0x4e7c2ce8f1f2874>) embark--vertico-selected)
  embark--targets()
  embark-act(nil)
  funcall-interactively(embark-act nil)
  call-interactively(embark-act nil nil)
  command-execute(embark-act)
  read-from-minibuffer("Find file: " "~/" (keymap (keymap (32)) keymap (10 . minibuffer-complete-and-exit) (13 . minibuffer-complete-and-exit) keymap (menu-bar keymap (minibuf "Minibuf" keymap (tab menu-item "Complete" minibuffer-complete :help "Complete as far as possible") (space menu-item "Complete Word" minibuffer-complete-word :help "Complete at most one word") (63 menu-item "List Completions" minibuffer-completion-help :help "Display all possible completions") "Minibuf")) (27 keymap (103 keymap (27 keymap (99 . switch-to-completions))) (118 . switch-to-completions)) (prior . switch-to-completions) (63 . minibuffer-completion-help) (32 . minibuffer-complete-word) (9 . minibuffer-complete) keymap (18 . consult-history) (menu-bar keymap (minibuf "Minibuf" keymap (previous menu-item "Previous History Item" previous-history-element :help "Put previous minibuffer history element in the min...") (next menu-item "Next History Item" next-history-element :help "Put next minibuffer history element in the minibuf...") (isearch-backward menu-item "Isearch History Backward" isearch-backward :help "Incrementally search minibuffer history backward") (isearch-forward menu-item "Isearch History Forward" isearch-forward :help "Incrementally search minibuffer history forward") (return menu-item "Enter" exit-minibuffer :key-sequence "\15" :help "Terminate input and exit minibuffer") (quit menu-item "Quit" abort-recursive-edit :help "Abort input and exit minibuffer") "Minibuf")) (13 . exit-minibuffer) (10 . exit-minibuffer) (7 . abort-minibuffers) (C-tab . file-cache-minibuffer-complete) (9 . self-insert-command) (XF86Back . previous-history-element) (up . previous-line-or-history-element) (prior . previous-history-element) (XF86Forward . next-history-element) (down . next-line-or-history-element) (next . next-history-element) (27 keymap (60 . minibuffer-beginning-of-buffer) (114 . previous-matching-history-element) (115 . next-matching-history-element) (112 . previous-history-element) (110 . next-history-element))) nil file-name-history "~/" nil)
  #f(compiled-function (prompt collection &optional predicate require-match initial-input hist def inherit-input-method) "Default method for reading from the minibuffer with completion.\nSee `completing-read' for the meaning of the arguments." #<bytecode 0x1295b6db419b26ae>)("Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/" nil)
  apply((#f(compiled-function (prompt collection &optional predicate require-match initial-input hist def inherit-input-method) "Default method for reading from the minibuffer with completion.\nSee `completing-read' for the meaning of the arguments." #<bytecode 0x1295b6db419b26ae>) "Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/" nil))
  vertico--advice(#f(compiled-function (prompt collection &optional predicate require-match initial-input hist def inherit-input-method) "Default method for reading from the minibuffer with completion.\nSee `completing-read' for the meaning of the arguments." #<bytecode 0x1295b6db419b26ae>) "Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/" nil)
  apply(vertico--advice #f(compiled-function (prompt collection &optional predicate require-match initial-input hist def inherit-input-method) "Default method for reading from the minibuffer with completion.\nSee `completing-read' for the meaning of the arguments." #<bytecode 0x1295b6db419b26ae>) ("Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/" nil))
  completing-read-default("Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/" nil)
  completing-read("Find file: " read-file-name-internal file-exists-p confirm-after-completion "~/" file-name-history "~/")
  read-file-name-default("Find file: " nil "~/" confirm-after-completion nil nil)
  read-file-name("Find file: " nil "~/" confirm-after-completion)
  find-file-read-args("Find file: " confirm-after-completion)
  byte-code("\300\301\302 \"\207" [find-file-read-args "Find file: " confirm-nonexistent-file-or-buffer] 3)
  call-interactively(find-file nil nil)
  command-execute(find-file)

```

### Consult-Keep-lines (from M-x) (consult package)
- keep-line but interactive
- Keep the line that matches the regex

### Tabspaces
- https://github.com/mclear-tools/tabspaces
- Trying about tabspaces library

## Day 6
- I tried pulling all the package and restart the emacs.
- It fixed the embark issue i am facing.
- Also check keybindings associated to embark that may cause some issue

### For Package management - Straight
- I used the following resources
- https://systemcrafters.cc/advanced-package-management/using-straight-el/

### Speed Type
- Practice touch typing from emacs
```
(straight-use-package 'speed-type)
```
- M-x speed-type-top-100 or speed-type-top-1000

### 6 Things every emacs user should consider - SystemCrafters Youtube video
- https://systemcrafters.net/emacs-from-scratch/the-best-default-settings/
- I didn't used all the stuff
- I like saving history of mini-buffer (awesome)
```
;; Save what you enter into minibuffer prompts
(setq history-length 30)
(savehist-mode 1)
```
- Get latest file from disk if it changes -> For file and dired
```
;; Revert buffers when the underlying file has changed
(global-auto-revert-mode 1)

;; Revert Dired and other buffers
(setq global-auto-revert-non-file-buffers t)

```
- Recent file mode seems great but not this time maybe later.

## Day 7 - IRC
- https://systemcrafters.cc/chatting-with-emacs/irc-basics-with-erc/
- M-x erc-tls
- By default librechat is selected so no need to change server and Port too.
- Before you join, you need to enter nick name and full name.
- After you login, `/join #<channel_name>`
- Get list of all channel, `/list`
- Disconnect `/part`
- IRC bouncer: Keep the connection to the IRC, Act as proxy between you and server which can persist the chats.
- More on IRC bouncer https://wiki.systemcrafters.cc/community/znc-bouncer-servers/

## Day 8 - Rewrite log diary function to save file as org
```
(defun log-diary()
  (interactive)
  (setq filename (concat "~/Documents/Diary/" (format-time-string "%Y-%m-%d") ".org"))
  (find-file filename)
  (insert (concat "* " (format-time-string "%H:%M") "\n\n"))
  (previous-line))
```
- Migrating the already present .md files to .org
```
for i in *.md ; do echo "$i" && pandoc -s $i -o $i.org ; done
```

## Day 9 - Org Modern package
- Written by minad
- Below config is copied from minad's ReadMe file.
```
(straight-use-package 'org-modern)
(add-hook 'org-mode-hook #'org-modern-mode)
(add-hook 'org-agenda-finalize-hook #'org-modern-agenda)

(dolist (face '(window-divider
                window-divider-first-pixel
                window-divider-last-pixel))
  (face-spec-reset-face face)
  (set-face-foreground face (face-attribute 'default :background)))
(set-face-background 'fringe (face-attribute 'default :background))

(setq
 ;; Edit settings
 org-auto-align-tags nil
 org-tags-column 0
 org-catch-invisible-edits 'show-and-error
 org-special-ctrl-a/e t
 org-insert-heading-respect-content t

 ;; Org styling, hide markup etc.
 org-hide-emphasis-markers t
 org-pretty-entities t
 org-ellipsis "…"

 ;; Agenda styling
 org-agenda-tags-column 0
 org-agenda-block-separator ?─
 org-agenda-time-grid
 '((daily today require-timed)
   (800 1000 1200 1400 1600 1800 2000)
   " ┄┄┄┄┄ " "┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄")
 org-agenda-current-time-string
 "⭠ now ─────────────────────────────────────────────────")

```

## Day 10 - Org agenda integration with Diary
```
(setq org-agenda-files '("~/Documents/Diary"))
```
- M x `org-agenda` and press t to see all the todo's.

## Day 11 - Custom Dashboard 
- Use a org file as startup page
```
(setq initial-buffer-choice "~/.config/doom/start.org")
```
