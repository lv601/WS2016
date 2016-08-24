# Git Zusammenfassung

## Git konfigurieren
```bash
# Setzt globale git Konfiguration
git config --global user.name="Max Mustermann"
git config --global user.mail="Max@Mustermann.at"
git config --global push.default=simple

# Zeigt Repository Konfiguration wenn in Repository
git config --list

# Zeigt globale git Konfiguration
git config --list --global
```

## Git Repository erstellen
```bash
# Erstellt ein leeres git repository
git init

# Erstellt ein leeres bare git Repository (ohne Arbeitsverzeichnis)
# bare Repositories erlauben git push
git init --bare # Github Repositories entsprechen bare Repositories
```

## Git Repository klonen
```bash
# Klone normales oder bare Repository
git clone <Repository Name>
```

## Git Workflow
```bash
# Hole letzte Änderungen vom remote Repository
git pull

# Löse Konflikte auf falls es welche gibt
# Füge Änderungen oder neue Files zum staging Bereich
git add <file1>
git add <file2>

# Schreibe Änderungen in Repository
git commit -m "Made changes in <file1> and <file2>"

# oder beides in einem (-a funktioniert nur bei Files die bereits im Repository sind)
git commit -a -m "Made changes in <file1> and <file2>"

# Änderungen auf das remote Repository laden (geht nur bei bare Repository)
git push
```
