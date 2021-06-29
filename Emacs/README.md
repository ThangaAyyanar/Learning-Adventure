# Emacs
- I have basic knowledge in vim related editor.
- Now i want to try the eternal long rival of vim **Emacs**.
- If i can combine the knowledge of both Vim + Emacs that would be awesome.

## Things i want to integrate
- [x] Git tools
- [x] Dashboard
- [ ] LSP (Language server)
  - [ ] Elisp
  - [x] Python
  - [x] Swift
- [ ] DAP (Debugging Adaptor)
  - [ ] Elisp
  - [ ] Python
  - [ ] Swift
- [ ] Ctags based navigation
- [ ] Easy to test software (use projectile test feature)
  - [ ] Elisp
  - [ ] Python
  - [ ] Swift
- [ ] Finance
  - [ ] Decide which software going to use
  - [ ] [GPG with Hledger](https://pzel.name/2016/07/18/Encrypted-hledger-with-emacs-and-gnupg.html)
    - [ ] hledger mode - For finance
- [ ] TRAMP integration (remote access the file)
- [ ] Use chemacs2 for emacs configuration.
- [ ] Applications
  - [ ] [Email client](https://macowners.club/posts/email-emacs-mu4e-macos/)
  - [ ] Explore elfeed
      - [ ] org elfeed (feed url from org)
  - [ ] Control mpd from emacs
  - [x] Epub book read - using nov
  - [x] PDF book read
    - Currently it is possible with doc mode but it is slow
    - May be give pdf-tools a try
- [x] Yas snippet
- [x] Markdown integration
- [x] Rest client integration (Emacs package verb)
- [x] PlantUML integration and Graphviz
- [x] [Speed typing](https://github.com/parkouss/speed-type)
- [x] [Speed reading](https://git.sr.ht/~iank/spray)
- [x] Auto Package update
- [x] Cheat.sh
- [x] Dash integration (Done using counsel-dash)
- [ ] Org Mode
    - [ ] Book tracking in emacs
    - [x] Use Effective org agenda. (I kindof understand how it works)
    - [x] Journaling. (Using structured template logic learned from SystemCrafters Video)
    - [ ] Org Roam.
    - [x] Org Habits
- [x] Perspective (Different session)
	- We can use tabs in emacs to achieve differnt window configuration.
	- But all buffers are visible.
  - For now it is not useful to me.
- [x] Gnupg integration

## Current Bugs i am facing
- [ ] After projectile switch, Fuzzy search is slow.
- [ ] SourceKit integration with iOS Library completion missing.

## Things i learned

- Ielm
  - M-x ielm (elsp eval loop)
  - Ctrl+J to evaluate current line and move to next line (This command can also be used in *scratch* buffer)

- Org mode
  - See inline image using (org-toggle-inline-images)
  - Narrowing C-x n s
  - Widening C-x n w

- Display tab bar in emacs
    - (global-tab-line-mode)

- set nowrap! in emacs
    - (toggle-truncate-lines)

## Youtube
- [System Crafters](https://www.youtube.com/c/SystemCrafters/playlists)
  - Emacs, Guix and EXWM related playlist and more.
- [Mike Zamansky](https://www.youtube.com/user/mzamansky/videos)

## Awesome emacs blogs
- https://macowners.club/posts/

## Auto update packages
- https://emacs.stackexchange.com/questions/31872/how-to-update-packages-installed-with-use-package/31904#31904

## Awesome emacs config
- https://github.com/mjago/Emacs/blob/master/init.org
- Awesome org related config - https://github.com/jparcill/emacs_config
- Distrotube emacs config - https://gitlab.com/dwt1/dotfiles/-/blob/master/.emacs.d.gnu/config.org
- https://gitlab.com/aimebertrand/dotfiles